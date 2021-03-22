# 风云-123
风云1-3 漫画; Fung Wan Comics;

# Getting Start

文件夹内包括风云3部曲和剑圣/步惊云外传。由于原始文件过大，这里仅仅放了网盘的下载链接。有需要的同学们，请自行到网盘进行下载。国外的同学推荐Google Drive，国内的同学请到百度云下载。欢迎各位同学把数据备份到各个网盘上，然后把分享链接加入到上述的5个文件夹下。

## JPG2PDF转换

以上分享是风云漫画的图片jpg格式，为了方便同学们阅读，我这里提供了一个图片转PDF的Python程序。


首先安装fpdf依赖:
```
pip install fpdf

```
运行以下命令，例如：
```
python fig2pdf.py "风云1"
```
就可以在**风云1**文件夹下找到合并后的PDF文件。


代码具体内容如下：

```python
import glob
from fpdf import FPDF
import sys
import os

if __name__ == '__main__':
    input_dir = sys.argv[1]
    os.chdir(input_dir)
    pdf = FPDF()
    #fpdf.set_compression(True)
    a = glob.glob("*/*.jpg")
    a = sorted(a)

    for image in a:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    
    saved_name = "{}.pdf".format(input_dir)
    print(saved_name)
    pdf.output(saved_name, "F")
```

由于转化后图片没有进行任何压缩，体积可能较大。同学们可以取消注释set_compression这行，对转化后PDF进行压缩。



