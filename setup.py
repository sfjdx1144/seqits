#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os
# python setup.py sdist 打包成tar.gz的形式
# python setup.py bdist_wheel  打包成wheel格式
try:
    with open(os.path.join(os.path.abspath(os.path.dirname("__file__")),"README.md")) as f:
        long_description=f.read()
except:
    long_description="Seqits"

setup(
    name="seqits",
    version="0.0.1",
    description="Tools for sequences process",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/sfjdx1144/seqits',
    author="Fujun Sun",
    author_email="sfjdx1144@live.com",
    packages=find_packages(),
    install_requires=['requests','argparse','colorama'],
    platforms="any",
    license="GNU GPLv3 Licence",
    python_requires=">=3.4.0",
    include_package_data=True
)