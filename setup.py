#!/usr/bin/env python
from setuptools import setup, find_packages

options = dict(
    name="janutils",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    description="Jan's utils.",
    long_description="Jan's utils.",
    author="Jan Pipek",
    author_email="jan.pipek@gmail.com",
    url="https://github.com/janpipek/janutils",
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

setup(**options)
