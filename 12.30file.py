# -*- coding: utf-8 -*-
"""
需求：把一堆.JAVA文件中的文本拿出来并保存到word中（做软著）
"""
from docx import Document#百度得到这个有趣强大的库
document = Document()
import os
def get_filename(path,filetype):
    name=[]
    for root,dirs,files in os.walk(path):

        for i in files:

            if filetype in i:

                name.append(i) 

    return name
name=get_filename('F:\\school\\rz\\2','java')#文件路径可以自己改
print(name)#得到文件中所有.java结尾的文件
data=[]
for file in name:
    document.add_heading(file)#以文件名为小标题
    f=open('F:\\school\\rz\\2\\'+file,encoding="utf-8")
    nr=f.read()
    paragraph = document.add_paragraph(nr)
    data.append(nr)           
    f.close()      
print(data)
document.save('test1.docx')