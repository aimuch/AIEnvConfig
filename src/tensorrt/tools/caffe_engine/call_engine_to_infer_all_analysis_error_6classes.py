import os
# import tensorflow as tf
import tensorrt as trt
from tensorrt.parsers import uffparser
import pycuda.driver as cuda
# import uff
import cv2
import numpy as np
from tqdm import tqdm



TEST_PATH = "/media/andy/Data/DevWorkSpace/Projects/imageClassifier/data/test"
# TEST_PATH = "/home/andy/caffe/examples/mydata/slot_classifier/data/train_extend/all"

TEST_OUT_PATH = "/media/andy/Data/DevWorkSpace/Projects/imageClassifier/data/test_out"

ENGINE_PATH = "/home/andy/caffe/examples/mydata/slot_classifier/engine/slot_6_model.engine"
# ENGINE_PATH = "/home/andy/caffe/examples/mydata/slot_classifier/engine/px2_classifier.engine"

OUTPUT_PATH = "./result/predict_out"

NET_INPUT_SHAPE = (256, 256)
NET_OUTPUT_SHAPE = 6
class_labels = ['error', 'half', 'invlb', 'invls', 'valid', 'corner']
# class_labels = ['valid_black', 'valid_leaf', 'valid_other', 'valid_shadow', 'valid_water', 'void_underground']

# Load Image
def load_image(img_path, net_input_shape):
    imgBGR = cv2.imread(img_path)
    img = cv2.resize(imgBGR, net_input_shape)
    # BGR -> RGB
    #img = img[:,:, (2, 1, 0)]

    ## Method 1
    # imgT = np.transpose(img, (2, 0, 1))  # c,w,h
    # imgF = np.asarray(imgT, dtype=np.float32)
    # mean = [[[88.159309]], [[97.966286]], [[103.66106]]] # Caffe image mean
    # imgS = np.subtract(imgF,mean)

    ## Method 2
    imgF = np.asarray(img, dtype=np.float32)
    mean = [128.0, 128.0, 128.0] # Caffe image mean
    # mean = [88.159309, 97.966286, 103.66106] # Caffe image mean
    imgSS = np.subtract(imgF, mean)/128.0
    imgS = np.transpose(imgSS, (2, 0, 1))  # c,w,h

    # RGB_MEAN_PIXELS = np.array([88.159309, 97.966286, 103.66106]).reshape((1,1,1,3)).astype(np.float32)

    return imgBGR, np.ascontiguousarray(imgS, dtype=np.float32) # avoid error: ndarray is not contiguous

def test_Loader(TEST_PATH, net_input_shape):
    label_list = []
    img_list = []
    imgBGR_list = []
    img_path_list = []
    per_class_num_dic = {}
    pair = []
    folders = os.listdir(TEST_PATH)
    for folder in folders:
        folder_path = os.path.join(TEST_PATH, folder)
        label = class_labels.index(folder)
        imgs = os.listdir(folder_path)
        img_num = len(imgs)
        per_class_num_dic[folder] = img_num
        for img in tqdm(imgs):
            img_path = os.path.join(folder_path, img)
            imgBGR, img = load_image(img_path, net_input_shape)
            img_list.append(img)
            imgBGR_list.append(imgBGR)
            img_path_list.append(img_path)
            label_list.append(label)
            pair.append((img, label))

    return pair, img_list, label_list, imgBGR_list, img_path_list, per_class_num_dic


def save_error(label, error_type, file_path):
    error_path = os.path.join(TEST_OUT_PATH, os.path.join(label, error_type))
    if not os.path.exists(error_path):
        os.makedirs(error_path)
    file_basename = os.path.basename(file_path)
    img = cv2.imread(file_path)
    dst_path = os.path.join(error_path, file_basename)
    cv2.imwrite(dst_path, img)

imgTestData = test_Loader(TEST_PATH, NET_INPUT_SHAPE)

# Load Engine file
G_LOGGER = trt.infer.ConsoleLogger(trt.infer.LogSeverity.ERROR)
engine = trt.utils.load_engine(G_LOGGER, ENGINE_PATH)
context = engine.create_execution_context()
runtime = trt.infer.create_infer_runtime(G_LOGGER)


# output = np.empty(1, dtype = np.float32)
# # Alocate device memory
# d_input = cuda.mem_alloc(1 * imgTestData[0][0][0].nbytes)
# d_output = cuda.mem_alloc(NET_OUTPUT_SHAPE * output.nbytes)
# bindings = [int(d_input), int(d_output)]
# stream = cuda.Stream()


predicts = []
pair = imgTestData[0]
imgBGRList = imgTestData[3]
imgPathList = imgTestData[4]
perClassNumDic = imgTestData[5]
p0 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p = 0

p0_to_1 = 0
p0_to_2 = 0
p0_to_3 = 0
p0_to_4 = 0
p0_to_5 = 0

p1_to_0 = 0
p1_to_2 = 0
p1_to_3 = 0
p1_to_4 = 0
p1_to_5 = 0

p2_to_1 = 0
p2_to_0 = 0
p2_to_3 = 0
p2_to_4 = 0
p2_to_5 = 0

p3_to_1 = 0
p3_to_2 = 0
p3_to_0 = 0
p3_to_4 = 0
p3_to_5 = 0

p4_to_1 = 0
p4_to_2 = 0
p4_to_3 = 0
p4_to_0 = 0
p4_to_5 = 0

p5_to_1 = 0
p5_to_2 = 0
p5_to_3 = 0
p5_to_4 = 0
p5_to_0 = 0


for (img, label), imgBGR, imgPath in zip(pair, imgBGRList, imgPathList):
    output = np.empty(NET_OUTPUT_SHAPE, dtype = np.float32)

    # Alocate device memory
    d_input = cuda.mem_alloc(1 * img.nbytes)
    d_output = cuda.mem_alloc(1 * output.nbytes)

    bindings = [int(d_input), int(d_output)]

    stream = cuda.Stream()
    # Transfer input data to device
    cuda.memcpy_htod_async(d_input, img, stream)
    # Execute model 
    context.enqueue(1, bindings, stream.handle, None)
    # Transfer predictions back
    cuda.memcpy_dtoh_async(output, d_output, stream)
    # Syncronize threads
    stream.synchronize()

    softmax = np.exp(output) / np.sum(np.exp(output))
    predict = np.argmax(softmax)
    predicts.append(predict)
    shape = np.shape(imgBGR)

    cv2.putText(imgBGR, str(predict), (shape[1]//2,shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 2 , (0, 0, 255), 2)
    img_dst_folder = os.path.join(OUTPUT_PATH, os.path.dirname(imgPath).split("/")[-1])
    if not os.path.exists(img_dst_folder):
        os.makedirs(img_dst_folder)
        # os.makedirs(img_dst_folder) # 可以递归创建
    img_dst_path = os.path.join(img_dst_folder, os.path.basename(imgPath))
    cv2.imwrite(img_dst_path, imgBGR)

    className = class_labels[label]

    # Calculate Precision
    if label == 0 and label != predict:
        if predict == 1:
            p0_to_1 += 1
            save_error(className, "p0_to_1", imgPath)
        if predict == 2:
            p0_to_2 += 1
            save_error(className, "p0_to_2", imgPath)
        if predict == 3:
            p0_to_3 += 1
            save_error(className, "p0_to_3", imgPath)
        if predict == 4:
            p0_to_4 += 1
            save_error(className, "p0_to_4", imgPath)
        if predict == 5:
            p0_to_5 += 1
            save_error(className, "p0_to_5", imgPath)
    elif label == 0 and label == predict:
        p0 += 1
        p += 1

    if label == 1 and label != predict:
        if predict == 0:
            p1_to_0 += 1
            save_error(className, "p1_to_0", imgPath)
        if predict == 2:
            p1_to_2 += 1
            save_error(className, "p1_to_2", imgPath)
        if predict == 3:
            p1_to_3 += 1
            save_error(className, "p1_to_3", imgPath)
        if predict == 4:
            p1_to_4 += 1
            save_error(className, "p1_to_4", imgPath)
        if predict == 5:
            p1_to_5 += 1
            save_error(className, "p1_to_5", imgPath)
    elif label == 1 and label == predict:
        p1 += 1
        p += 1

    if label == 2 and label != predict:
        if predict == 0:
            p2_to_0 += 1
            save_error(className, "p2_to_0", imgPath)
        if predict == 1:
            p2_to_1 += 1
            save_error(className, "p2_to_1", imgPath)
        if predict == 3:
            p2_to_3 += 1
            save_error(className, "p2_to_3", imgPath)
        if predict == 4:
            p2_to_4 += 1
            save_error(className, "p2_to_4", imgPath)
        if predict == 5:
            p2_to_5 += 1
            save_error(className, "p2_to_5", imgPath)
    elif label == 2 and label == predict:
        p2 += 1
        p += 1

    if label == 3 and label != predict:
        if predict == 0:
            p3_to_0 += 1
            save_error(className, "p3_to_0", imgPath)
        if predict == 1:
            p3_to_1 += 1
            save_error(className, "p3_to_1", imgPath)
        if predict == 2:
            p3_to_2 += 1
            save_error(className, "p3_to_2", imgPath)
        if predict == 4:
            p3_to_4 += 1
            save_error(className, "p3_to_4", imgPath)
        if predict == 5:
            p3_to_5 += 1
            save_error(className, "p3_to_5", imgPath)
    elif label == 3 and label == predict:
        p3 += 1
        p += 1

    if label == 4 and label != predict:
        if predict == 0:
            p4_to_0 += 1
            save_error(className, "p4_to_0", imgPath)
        if predict == 1:
            p4_to_1 += 1
            save_error(className, "p4_to_1", imgPath)
        if predict == 2:
            p4_to_2 += 1
            save_error(className, "p4_to_2", imgPath)
        if predict == 3:
            p4_to_3 += 1
            save_error(className, "p4_to_3", imgPath)
        if predict == 5:
            p4_to_5 += 1
            save_error(className, "p4_to_5", imgPath)
    elif label == 4 and label == predict:
        p4 += 1
        p += 1

    if label == 5 and label != predict:
        if predict == 0:
            p5_to_0 += 1
            save_error(className, "p5_to_0", imgPath)
        if predict == 1:
            p5_to_1 += 1
            save_error(className, "p5_to_1", imgPath)
        if predict == 2:
            p5_to_2 += 1
            save_error(className, "p5_to_2", imgPath)
        if predict == 3:
            p5_to_3 += 1
            save_error(className, "p5_to_3", imgPath)
        if predict == 4:
            p5_to_4 += 1
            save_error(className, "p5_to_4", imgPath)
    elif label == 5 and label == predict:
        p5 += 1
        p += 1
    # 将错误识别成有效车位以及有效车位识别错误的打印出来
    img_dst_folder_4 = img_dst_folder + "_"
    if not os.path.exists(img_dst_folder_4):
        os.makedirs(img_dst_folder_4)
    if ((label == 0 or label == 1 or label ==2 or label == 3 or label == 5) and predict == 4) or (label==4 and predict != 4):
        img_dst_path_4 = os.path.join(img_dst_folder_4, os.path.basename(imgPath))
        cv2.imwrite(img_dst_path_4, imgBGR)


    print("True = ",label, ", predict = ", predict, ", softmax = ", softmax)


grandTrue = np.array(imgTestData[1][1])
predicts = np.array(predicts)
error = predicts[predicts!=grandTrue]

print(imgTestData[1][1])
print("-------")
print(predicts)
print("-------")
print(len(error))
print((len(imgTestData[0])-len(error))/len(imgTestData[0]))

print(perClassNumDic)


print("p0_to_1=",p0_to_1)
print("p0_to_2=",p0_to_2)
print("p0_to_3=",p0_to_3)
print("p0_to_4=",p0_to_4)
print("p0_to_5=",p0_to_5)
print("sum error num = ", p0_to_1+p0_to_2+p0_to_3+p0_to_4+p0_to_5)
print("this=",p0, " total=", perClassNumDic[class_labels[0]])
print("p0=",p0/perClassNumDic[class_labels[0]])
print("\t")

print("p1_to_0=",p1_to_0)
print("p1_to_2=",p1_to_2)
print("p1_to_3=",p1_to_3)
print("p1_to_4=",p1_to_4)
print("p1_to_5=",p1_to_5)
print("this=",p1, " total=", perClassNumDic[class_labels[1]])
print("p1=",p1/perClassNumDic[class_labels[1]])
print("\t")

print("p2_to_0=",p2_to_0)
print("p2_to_1=",p2_to_1)
print("p2_to_3=",p2_to_3)
print("p2_to_4=",p2_to_4)
print("p2_to_5=",p2_to_5)
print("this=",p2, " total=", perClassNumDic[class_labels[2]])
print("p2=",p2/perClassNumDic[class_labels[2]])
print("\t")

print("p3_to_0=",p3_to_0)
print("p3_to_1=",p3_to_1)
print("p3_to_2=",p3_to_2)
print("p3_to_4=",p3_to_4)
print("p3_to_5=",p3_to_5)
print("this=",p3, " total=", perClassNumDic[class_labels[3]])
print("p3=",p3/perClassNumDic[class_labels[3]])
print("\t")

print("p4_to_0=",p4_to_0)
print("p4_to_1=",p4_to_1)
print("p4_to_2=",p4_to_2)
print("p4_to_3=",p4_to_3)
print("p4_to_5=",p4_to_5)
print("this=",p4, " total=", perClassNumDic[class_labels[4]])
print("p4=",p4/perClassNumDic[class_labels[4]])
print("\t")

print("p5_to_0=",p5_to_0)
print("p5_to_1=",p5_to_1)
print("p5_to_2=",p5_to_2)
print("p5_to_3=",p5_to_3)
print("p5_to_4=",p5_to_4)
print("this=",p5, " total=", perClassNumDic[class_labels[5]])
print("p5=",p5/perClassNumDic[class_labels[5]])
print("\t")
print("p=",p/sum(perClassNumDic.values()))