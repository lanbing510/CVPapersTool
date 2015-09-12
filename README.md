# CVPapers论文整理小工具

## 工具介绍及运行实例

相信计算机视觉领域的同道中人都知道这个Computer Vision Resource网站， http://www.cvpapers.com/  网页部分截图如下：

<img src="https://github.com/lanbing510/CVPaperTool/raw/master/screenshots/cvpapers.jpg" width="60%" height="60%">

可以看到有太多论文集，比如CVPR2013年就有472篇，自己写了一个小工具，用来筛选感兴趣的论文
运行界面如下：

<img src="https://github.com/lanbing510/CVPaperTool/raw/master/screenshots/ui.jpg" width="60%" height="60%">

输入论文集网址和自己感兴趣的领域点击提交即可，其中关键字可以输入多个（不区分大小写），然后程序会按相关度从高到底的顺序给出论文列表
提交后运行部分截图如下：

<img src="https://github.com/lanbing510/CVPaperTool/raw/master/screenshots/result.jpg" width="60%" height="60%">

这样可以大大减少我们筛选的工作量，然后自己可以再对要读的论文在后面的复选框做上标记

## 工具使用和进一步开源开发

1 运行输入cmd

2 cd 进入所下载文件pl所在目录

3 建议基于web的服务器：即输入python -m CGIHTTPServer

4 在浏览器窗口输入http://localhost:8000/pl.htm 即可使用

注 Python需要BeautifulSoup工具包，可在https://pypi.python.org/pypi/setuptools#windows-powershell-3-or-later 下载easy_install后 进行easy_install beautifulsoup 即可

很早之前做的，欢迎感兴趣者开发完善，只要会python，在此基础上很容易做扩展。
