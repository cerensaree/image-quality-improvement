#!/usr/bin/env python

from setuptools import find_packages, setup

import os
import subprocess
import time


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


if __name__ == '__main__':
    setup(
        name='gfpgan',
        description='GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author="Ceren Sare Kilicarslan",
        author_email="cerensare.06@gmail.com",
        keywords='computer vision, pytorch, image restoration, super-resolution, face restoration, gan, gfpgan',
        include_package_data=True,
        packages=find_packages(exclude=('options', 'datasets', 'experiments', 'results', 'tb_logger', 'wandb')),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='Apache License Version 2.0',
        setup_requires=['cython', 'numpy'],
        install_requires=get_requirements(),
        zip_safe=False)
