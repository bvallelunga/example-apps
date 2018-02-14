#!/usr/bin/env python3

import os
from setuptools import setup, find_packages


def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()


a = setup(
  name = "sentiment",
  version = "0.0.1",
  description = "Learning to Generate Reviews and Discovering Sentiment",
  license = "MIT License",
  long_description=read('README.md'),
  keywords = "generating reviews discovering sentiment",
  url = "https://github.com/openai/generating-reviews-discovering-sentiment",
  packages=[],
  install_requires=[
    "tqdm",
    "sklearn",
    "tensorflow",
    "numpy",
    
  ],
  classifiers=[
    "Topic :: Utilities",
    "License :: MIT License"
  ]
)