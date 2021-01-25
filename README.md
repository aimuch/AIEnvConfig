# AI on Ubuntu Platform

AI实验环境搭建和深度学习算法

**安装环境**
*其他平台环境类似*
```vim
硬件： ROG MAXIMUS XII HERO(WI-FI) / NVIDIA GTX 2080TI / DDR4 64G 3600 / SSD 2T / HDD 4T
系统： Ubuntu-16.04-64bit / Ubuntu-18.04-64bit / Windows 10 Professional
软件： CUDA9.0-CUDA11.2 /cuDNN/TensorRT/OpenCV/caffe/YOLO/Protobuf/Matlab/VIM
```
---
### 目录
1. [**AI基础环境搭建和设置**](src/ai_base_env.md#ai基础环境搭建和设置)
   1. [安装Ubuntu和Windows双系统](src/ai_base_env.md#安装ubuntu和windows双系统)
       - [有关Ubuntu分区的相关问题](src/ai_base_env.md#有关ubuntu分区的相关问题)
       - [Ubuntu与Windows双系统时间同步解决方法](src/ai_base_env.md#ubuntu与windows双系统时间同步解决方法)
       - [调整grub引导系统顺序](src/ai_base_env.md#调整grub引导系统顺序)
       - [设置grub引导菜单的分辨率](src/ai_base_env.md#设置grub引导菜单的分辨率)
       - [设置grub Menu显示](src/ai_base_env.md#设置grub-menu显示)
   2. [安装**NVIDIA驱动**](src/ai_base_env.md#安装nvidia驱动)
       - [安装NVIDIA驱动所需的依赖包](src/ai_base_env.md#安装nvidia驱动所需的依赖包)
       - [禁用Ubuntu自带的显卡驱动](src/ai_base_env.md#禁用ubuntu自带的显卡驱动)
       - [Ubuntu16TLS安装NVIDIA驱动](src/ai_base_env.md#ubuntu16tls安装nvidia驱动)
       - [Ubuntu18TLS安装NVIDIA驱动](src/ai_base_env.md#ubuntu18tls安装nvidia驱动)
       - [配置NVIDIA环境变量](src/ai_base_env.md#配置环境变量)
       - [查看NVIDIA显卡驱动版本](src/ai_base_env.md#查看nvidia驱动版本)
       - [解决Linux双系统安装卡在启动Logo](src/ai_base_env.md#解决linux双系统安装卡在启动logo)
   3. [安装**CUDA**](src/ai_base_env.md#安装cuda)
       - [安装CUDA步骤](src/ai_base_env.md#安装cuda步骤)
       - [修改配置文件](src/ai_base_env.md#修改配置文件)
       - [查看CUDA版本](src/ai_base_env.md#查看cuda版本)
       - [卸载CUDA的方法](src/ai_base_env.md#卸载cuda的方法)
   4. [安装**cuDNN**](src/ai_base_env.md#安装cudnn)
       - [下载安装**cuDNN**](src/ai_base_env.md#下载安装cudnn)
       - [**cuDNN**常见问题](src/ai_base_env.md#cudnn常见问题)
   5. [**Ubuntu CUDA多版本**问题](src/ai_base_env.md#ubuntu-cuda多版本问题)
   6. [**Windows CUDA多版本**问题](src/ai_base_env.md#windows-cuda多版本问题)
   7. [**Anaconda**](src/ai_base_env.md#anaconda)
       - [安装Anaconda](src/ai_base_env.md#安装anaconda)
       - [屏蔽Anaconda](src/ai_base_env.md#屏蔽anaconda)
       - [重建Anaconda软连接](src/ai_base_env.md#重建anaconda软连接)
       - [Anaconda虚拟环境](src/ai_base_env.md#anaconda虚拟环境)
       - [卸载Anaconda](src/ai_base_env.md#卸载anaconda)
   8. [安装**OpenCV**](src/ai_base_env.md#安装opencv)
       - [下载OpenCV](src/ai_base_env.md#下载opencv)
       - [编译OpenCV](src/ai_base_env.md#编译opencv)
       - [安装OpenCV](src/ai_base_env.md#安装opencv)
       - [卸载OpenCV](src/ai_base_env.md#卸载opencv)
   9.  [安装**Docker**](src/ai_base_env.md#安装docker)
   10. [**TensorRT**](src/ai_base_env.md#tensorrt)
       - [安装TensorRT](src/ai_base_env.md#安装tensorrt)
         - [TensorRT环境变量设置](src/ai_base_env.md#tensorrt1)
         - [安装Python的TensorRT包](src/ai_base_env.md#tensorrt2)
         - [安装uff](src/ai_base_env.md#tensorrt3)
         - [安装graphsurgeon](src/ai_base_env.md#tensorrt4)
         - [验证TensorRT是否安装成功](src/ai_base_env.md#tensorrt5)
         - [TensorRT安装过程中遇到的问题以及解决方法](src/ai_base_env.md#tensorrt6)
       - [TensorRT生成**Engine**](src/ai_base_env.md#tensorrt生成engine)
         - [**Caffe**模型用TensorRT生成Engine](src/ai_base_env.md#caffe模型用tensorrt生成engine)
         - [**TensorFlow**模型用TensorRT生成**Engine**](src/ai_base_env.md#tensorflow模型用tensorrt生成engine)
           - [将TensorFlow模型生成**UFF**文件](src/ai_base_env.md#将tensorflow模型生成uff文件)
           - [将**UFF**文件转为**Engine**](src/ai_base_env.md#将uff文件转为engine)
           - [调用**Engine**进行推理](src/ai_base_env.md#调用engine进行推理)
         - [TensorRT官方实例](src/ai_base_env.md#tensorrt官方实例) >> **资料在**[**src/tensorrt**](src/tensorrt)
           - [TensorRT Caffe Engine](./src/tensorrt/tensorrt-4.0.1.6/caffe_to_tensorrt.ipynb)
           - [TensorRT Tensorflow Engine](./src/tensorrt/tensorrt-4.0.1.6/tf_to_tensorrt.ipynb)
           - [Manually Construct Tensorrt Engine](./src/tensorrt/tensorrt-4.0.1.6/manually_construct_tensorrt_engine.ipynb)
   11. [安装**Pytorch**](src/ai_base_env.md#安装pytorch)
   12. [安装**TensorFlow**](src/ai_base_env.md#安装tensorflow)
   13. [安装**Caffe**](src/ai_base_env.md#安装caffe)
       - [Python2下安装Caffe](src/ai_base_env.md#python2下安装cafe)
       - [Python3下安装Caffe](src/ai_base_env.md#python3下安装cafe)
   14. [安装Protobuf](src/ai_base_env.md#安装protobuf)
   15. [Linux MATLAB安装](src/ai_base_env.md#linux-matlab安装)
       - [MATLAB 2018安装](src/ai_base_env.md#linux-matlab2018安装)
       - [MATLAB 2019安装](src/ai_base_env.md#linux-matlab2019安装)

2. [**AI Algorithms**](./src/ai_algorithms.md)
     - [YOLO V3](src/ai_algorithms.md#yolo-v3)
     - [Faster R-CNN](./src/ai_algorithms.md#faster-r-cnn)
     - [Anaconda FAQ](./src/ai_algorithms.md#anaconda-faq)
       - [Anaconda环境下TensorFlow和Pytorch共存问题](./src/ai_algorithms.md#anaconda环境下tensorflow和pytorch共存问题)
       - [Anaconda环境下Python下导入正常Jupyter Notebook中导入莫名出错](./src/ai_algorithms.md#anaconda环境下python下导入正常jupyter-notebook中导入莫名出错)
     - [深度学习服务器FAQ](./src/ai_server_FAQ.md#深度学习服务器faq)
       - [docker常用命令](./src/ai_server_FAQ.md#docker常用命令)
       - [多显卡训练问题](./src/ai_server_FAQ.md#多显卡训练问题)
       - [远程访问服务器**Jupyter Notebook**](./src/ai_server_FAQ.md#远程访问服务器jupyter-notebook)
         - [方法1 ssh远程使用jupyter notebook](./src/ai_server_FAQ.md#方法1-ssh远程使用jupyter-notebook)
         - [方法2 利用jupyter notebook自带的远程访问功能](./src/ai_server_FAQ.md#方法2-利用jupyter-notebook自带的远程访问功能)
     - [Transfer Learning](src/ai/transfer-learning.md#transfer-learning)
     - [**Loss Function**](src/ai/loss-function.md#loss-function)
        - [Loss Function简介](src/ai/loss-function.md#loss-function简介)
        - [Loss Function种类](src/ai/loss-function.md#loss-function种类)
     - [**神经网络参数量(weights)和计算量(FLOPs)**](src/ai/weights.md)
     - [**特征尺寸(Feature Map)和感受野(Receptive Field)计算**](src/ai/receptive_field.md)

3. [**AI Framework**](src/ai_framework.md#ai-framework)
    - [AI 常用的结构框架](src/ai_framework.md#ai框架数据结构)
    - [**TensorFlow**](src/ai/tensorflow.md#tensorflow)
      - [Tensorflow to TensorRT Image Classification](src/ai/tensorflow.md#tensorflow-to-tensorrt-image-classification)
      - [TensorFlow FAQ](src/ai/tensorflow.md#tensorflow-faq)
    - [**Pytorch**](src/ai/pytorch.md#pytorch)
      - [将数据转换为Pytorch格式](src/ai/pytorch.md#将数据转换为pytorch格式)
    - [**Caffe**](src/ai/caffe.md#caffe)
      - [Caffe训练模型可视化](src/ai/caffe.md#caffe训练模型可视化)
4. [**AI Model Optimization**](./src/ai_model_optimization.md)
      - [网络量化](./src/ai_model_optimization.md#网络量化)
      - [网络剪枝](./src/ai_model_optimization.md#网络剪枝)
5. [**AI Tools**](./src/ai_tools.md)
     - [Netron](./src/ai_tools.md#Netron)
6. [**Ubuntu FAQ**](./src/linux_env_set.md#ubuntu-faq)
     - [**Awesome Software**](./src/linux_env_set.md#awesome-linux-software)
     - [Linux环境变量初始化与对应文件的生效顺序](./src/linux_env_set.md#linux环境变量初始化与对应文件的生效顺序)
     - [**Ubuntu Library**](./src/linux_library.md#ubuntu-library)
       - [Eigen](./src/linux_library.md#eigen)
     - [**Docker**安装与使用](./src/linux_env_set.md#docker安装与使用)
       - [Docker安装](./src/linux_env_set.md#docker安装)
       - [Docker使用](./src/linux_env_set.md#docker使用)
     - [**Linuxbrew**安装](./src/linux_env_set.md#linuxbrew安装)
       - [安装linuxbrew](./src/linux_env_set.md#安装linuxbrew)
       - [linuxbrew必装包](./src/linux_env_set.md#linuxbrew必装包)
       - [brew常用命令](./src/linux_env_set.md#brew常用命令)
       - [linuxbrew注意事项](./src/linux_env_set.md#linuxbrew注意事项)
     - [监视GPU和CPU资源利用情况](./src/linux_env_set.md#监视gpu和cpu资源利用情况)
     - [Ubuntu每次开机后提示检测到系统程序出现问题的解决方法](./src/linux_env_set.md#ubuntu每次开机后提示检测到系统程序出现问题的解决方法)
     - [Ubuntu循环登陆问题](./src/linux_env_set.md#ubuntu循环登陆问题)
     - [文件夹打开缓慢](./src/linux_env_set.md#文件夹打开缓慢)
     - [安装Python依赖库](./src/linux_env_set.md#安装python依赖库)
       - [Python基础库安装](./src/linux_env_set.md#python基础库安装)
       - [Python项目requirements文件的生成和使用](./src/linux_env_set.md#python项目requirements文件的生成和使用)
     - [安装Chrome浏览器](./src/linux_env_set.md#安装chrome浏览器)
     - [pip **/** pip3常见报错](./src/linux_env_set.md#pip和pip3常见报错)
     - [关于Ubuntu 16.04LTS下安装Spyder3的问题](./src/linux_env_set.md#ubuntu-16下安装spyder3)
     - [安装Teamviewer](./src/linux_env_set.md#安装teamviewer)
     - [安装搜狗输入法](./src/linux_env_set.md#安装搜狗输入法)
     - [WPS设置](./src/linux_env_set.md#wps设置)
       - [解决WPS启动提示字体未安装错误](./src/linux_env_set.md#解决wps启动提示字体未安装错误)
       - [WPS切换显示语言](./src/linux_env_set.md#wps切换显示语言)
       - [WPS不能输入中文](./src/linux_env_set.md#wps不能输入中文)
     - [安装赛睿霜冻之蓝V2驱动](./src/linux_env_set.md#安装赛睿霜冻之蓝v2驱动)
     - [**zsh** **oh-my-zsh**默认shell的最佳替代品](./src/linux_env_set.md#zsh-oh-my-zsh默认shell的最佳替代品)
       - [查看系统shell环境](./src/linux_env_set.md#查看系统shell环境)
       - [安装**zsh**](./src/linux_env_set.md#安装zsh)
       - [安装**vimrc**](./src/linux_env_set.md#安装vimrc)
       - [安装**oh-my-zsh**](./src/linux_env_set.md#安装oh-my-zsh)
       - [安装**zsh-autosuggestions**](./src/linux_env_set.md#安装zsh-autosuggestions)
       - [安装**zsh-syntax-highlighting**](./src/linux_env_set.md#安装zsh-syntax-highlighting)
       - [安装**colorls**](./src/linux_env_set.md#安装colorls)
       - [安装**fzf**](./src/linux_env_set.md#安装fzf)
       - [安装**navi**](./src/linux_env_set.md#安装navi)
     - [**vim**配置](./src/linux_env_set.md#vim配置)
       - [YouCompleteMe实现vim自动补全](./src/linux_env_set.md#youcompleteme实现vim自动补全)
       - [vim最终配置](./src/linux_env_set.md#vim最终配置)
     - [**Tmux**配置与使用](./src/linux_env_set.md#tmux配置与使用)
       - [Tmux配置](./src/linux_env_set.md#tmux配置)
       - [Tmux使用手册](./src/linux_env_set.md#tmux使用手册)
     - [**FFmpeg的使用教程**](./src/ffmpeg.md)
     - [远程连接Ubuntu](./src/linux_env_set.md#远程连接ubuntu)
     - [**Sublime Text 3**配置问题](./src/linux_env_set.md#sublime-text-3配置问题)
     - [**VSCode**配置问题](./src/linux_env_set.md#vscode配置问题)
       - [**Awesome VScode Plugin**](./src/linux_env_set.md#awesome-vscode-plugin)
       - [VScode Tips](./src/linux_env_set.md#vscode-tips)
       - [Ubuntu VScode配置Cpp编译环境](./src/linux_env_set.md#ubuntu-vscode配置cpp编译环境)
       - [VScode环境配置](./src/linux_env_set.md#vscode环境配置)
     - [Ubuntu查看和关闭进程](./src/linux_env_set.md#ubuntu查看和关闭进程)
     - [Ubuntu后台执行命令](./src/linux_env_set.md#ubuntu后台执行命令)
     - [Ubuntu程序开机自启](./src/linux_env_set.md#ubunt程序开机自启)
        - [修改系统启动文件](./src/linux_env_set.md#修改系统启动文件)
        - [Startup Applications](./src/linux_env_set.md#startup-applications)
     - [查看系统状态](./src/linux_env_set.md#查看系统状态)
     - [**彻底卸载**软件](./src/linux_env_set.md#彻底卸载软件)
     - [**ESXi下安装iKuai和LEDE双软路由**](src/softRoute/softroute.md#esxi下安装ikuai和lede双软路由)
       - [网络拓扑图](src/softRoute/softroute.md#网络拓扑图)
       - [ESXi](src/softRoute/softroute.md#esxi)
       - [iKuai](src/softRoute/softroute.md#ikuai)
       - [LEDE](src/softRoute/softroute.md#lede)
       - [设置iKuai和LEDE开机自动启动](src/softRoute/softroute.md#设置ikuai和lede开机自动启动)
     - [NanoPi-R1烧写系统](./src/nanopi-r1.md)
     - [GL-iNet AR750 官方固件安装SSR Plus插件](./src/GL-iNet-AR750-官方固件安装SSR-Plus-插件.md)
     - [**Shadowsocks**安装](./src/ss.md#shadowsocks安装)
       - [Shadowsocks说明](./src/ss.md#shadowsocks说明)
       - [安装Shadowsocks-qt5](./src/ss.md#安装shadowsocks-qt5)
       - [安装electron-ssr](./src/ss.md#安装electron-ssr)
       - [配置Chrome浏览器](./src/ss.md#配置chrome浏览器)
     - [**Ubuntu 美化**](./src/linux_env_set.md#ubuntu-美化)
       - [Unity环境](./src/linux_env_set.md#unity环境)
       - [GNOME环境](./src/linux_env_set.md#gnome环境)
     - [Ubuntu启动后GUI界面卡住不动](./src/linux_env_set.md#ubuntu启动后gui界面卡住不动)
     - [Ubuntu1804使用过程中常遇到的问题](./src/linux_env_set.md#ubuntu1804使用过程中长遇到的问题)
7. [**参考资料**](#参考资料)
<!-- 8.  [Sponsor](#sponsor) -->
---

## TODO
- [x] 模型大小(参数量)估计
- [x] 感受野计
- [ ] 语义分割
- [ ] 网络优化
- [ ] TensorRT自定义层
- [ ] Pytorch model => OONX
- [ ] TensorFlow model => OONX
- [ ] Caffe 源码解读
- [ ] Darknet 源码解读
- [ ] 目标追踪


<!-- # Sponsor
![wechat](src/Sponsor/wechat.JPG)
![alipay](src/Sponsor/alipay.JPG) -->

---
##  参考资料
> 1. [win10下安装Ubuntu16.04双系统](https://blog.csdn.net/s717597589/article/details/79117112/)
> 2. [Ubuntu 16.04+CUDA 9.1+cuDNN v7+OpenCV 3.4.0+Caffe+PyCharm 完全安装指南](https://blog.csdn.net/balixiaxuetian/article/details/79154013)
> 3. [cuDNN官方安装指导](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux)
> 4. [ubuntu16.04+caffe+cpu+Anaconda3(python3)](https://blog.csdn.net/m0_38116269/article/details/85098640)
> 5. [caffe编译遇到的问题](https://blog.csdn.net/m0_37407756/article/details/70789271)
> 6. [linux安装MATLAB R2018a步骤](https://blog.csdn.net/m0_37775034/article/details/80876362)
> 7. [关于Ubuntu16.04LTS下Python版本和安装Spyder3的问题？](https://www.zhihu.com/question/51248022/answer/142596984)
> 8. [zsh + oh-my-zsh 默认shell的最佳替代品](https://blog.phpgao.com/oh-my-zsh.html)
> 9. [Terminal Experience](https://medium.com/@caulfieldOwen/youre-missing-out-on-a-better-mac-terminal-experience-d73647abf6d7)
> 10. [远程访问服务器Jupyter Notebook的方法](https://www.jianshu.com/p/8fc3cd032d3c)
> 11. [Jupyer Notebook官方指南](https://jupyter-notebook.readthedocs.io/en/latest/public_server.html#notebook-server-security)
> 12. [设置 jupyter notebook 可远程访问](https://blog.csdn.net/simple_the_best/article/details/77005400)
> 13. [Docker — 从入门到实践](https://github.com/yeasy/docker_practice)
> 14. [Docker 官方 Ubuntu 安装文档](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
> 15. [.tmux配置](https://github.com/gpakosz/.tmux)
> 16. [Tmux 快捷键 & 速查表](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7)
> 17. [TensorRT官方安装指南](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html)
> 18. [Anaconda官方给出的卸载方法](http://docs.anaconda.com/anaconda/install/uninstall/)
> 19. [Eigen是个什么鬼？](https://zhuanlan.zhihu.com/p/36706885)
> 20. [AW 17 R5 i9 Ubuntu? Linux?](https://www.dell.com/community/Alienware/AW-17-R5-i9-Ubuntu-Linux/td-p/6109054)
> 21. [Alienware 17 R4 Ubuntu 16.04 WiFi driver](https://askubuntu.com/questions/1016903/alienware-17-r4-ubuntu-16-04-wifi-driver)
> 22. [如何计算感受野(Receptive Field)——原理](https://zhuanlan.zhihu.com/p/31004121)
> 23. [A guide to receptive field arithmetic for Convolutional Neural Networks](https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutional-neural-networks-e0f514068807)
> 24. [关于感受野 (Receptive field) 你该知道的事](https://iphysresearch.github.io/posts/receptive_field.html)
> 25. [特征图尺寸和感受野计算详解](https://zhuanlan.zhihu.com/p/56940729)
> 26. [卷积神经网络中的感受野计算（译）](https://zhuanlan.zhihu.com/p/26663577)
> 27. [神经网络参数量的计算: 以UNet为例](https://zhuanlan.zhihu.com/p/57437131)
> 28. [从AlexNet理解卷积神经网络的一般结构](https://blog.csdn.net/chaipp0607/article/details/72847422)
> 29. [经典神经网络参数的计算](https://zhuanlan.zhihu.com/p/49842046)
> 30. [Ubuntu 18.04 NVIDIA驱动安装总结](https://blog.csdn.net/tjuyanming/article/details/80862290)
> 31. [解决Linux双系统安装卡在启动Logo](https://blog.csdn.net/tjuyanming/article/details/79267984)
> 32. [Ubuntu 18.04 安装 NVIDIA 显卡驱动](https://zhuanlan.zhihu.com/p/59618999)
> 33. [windows下同一个显卡配置多个CUDA工具包以及它们之间的切换](https://blog.csdn.net/qq_27825451/article/details/89135592)   
> 34. [Netron](https://github.com/lutzroeder/netron)
> 35. [Ubuntu 18.04安装Docker CE及NVIDIA Container Toolkit流程](https://www.cnblogs.com/journeyonmyway/p/11234572.html)    
> 36. [NVIDIA Installing on Ubuntu and Debian](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)