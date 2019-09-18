#!/usr/bin/python
# -*- coding: UTF-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplified-scrapy",
    version="0.0.1",
    author="yiyedata",
    author_email="3095069599@qq.com",
    description="A Simple Distributed Web Crawle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yiyedata/simplified-scrapy",
    packages=setuptools.find_packages(),
    include_package_data=True,    # 自动打包文件夹内所有数据
    zip_safe=True,                # 设定项目包为安全，不用每次都检测其安全性
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)