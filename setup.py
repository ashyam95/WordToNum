# -*- coding: utf-8 -*-
'''
Created on Wed Sep 26 17:15:34 2018

@author: azubair
'''

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='WordToNum',
    version='0.0.1',
    author='Ashyam Zubair',
    author_email='ashyamzubair@gmail.com',
    description='Converts word in string to actual number',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)