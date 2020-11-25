# data_transfer
this program is used to transfer data from voc2yolo

**step1**：下载我的代码（or自己建立如上图文件结构，注意此时文件夹都是空的）
				https://github.com/hellogithubsir/data_transfer.git
**step2**：路径中把VOC数据形式的标签放入Annotations，图片放入images中
**step3**：运行01，02，03后，
最后:my_datasets就是最后我们要的数据文件夹，“my_datasets”文件夹名字改成你自己要的
**PS**：因为懒得考虑多种意外形式，没做容错处理，但是只要按照我步骤来就没问题。如果真的出来什么问题文件结构如上图所示重来一次就不会出错，公司里也一直用的是这个程序。

下面演示流程及对应输出结果：
**step1**：下载我的代码（or自己建立如上图文件结构，注意此时文件夹都是空）
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020112511020824.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1Njc5NzAx,size_16,color_FFFFFF,t_70#pic_center)
**step2**：路径中把VOC数据形式的标签放入Annotations，图片放入images中，“my_datasets”文件夹名字改成你自己的
可以看到已经由空的编程可以文件展开的形式，这里图片太多所以没在载入完我就截图了
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201125110807424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1Njc5NzAx,size_16,color_FFFFFF,t_70#pic_center)

**step3**：
运行01，在main文件夹下出现了4个txt
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201125111351712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1Njc5NzAx,size_16,color_FFFFFF,t_70#pic_center)
运行02后
出现了6个txt，其中*_sets_directory.txt就是第一部分中提到的YOLOV5支持的第二种形式，就是很多教程中的train.txt，test.txt，个人认为很容易与main中的同名文件混淆，所以我这里改了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201125111557398.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1Njc5NzAx,size_16,color_FFFFFF,t_70#pic_center)

运行03后
可以看见my_datasets下的空文件夹编程了可展开的形式，“my_datasets”实际中根据自己需求改名字，它就是最后我们要的数据集，直接移走使用就行。
PS:我这里是将images和labels的文件移动到对应文件家下，如果想保留的话将03代码26行的move改为copy就行了
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201125112409690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1Njc5NzAx,size_16,color_FFFFFF,t_70#pic_center)
