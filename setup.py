"""Multidimensional LSTMs for TensorFlow.
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
here  =  path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding = "utf-8") as stream:
    long_description  =  stream.read()

setup(
    name = "tfndlstm",
    version = "0.0.2",
    description = "Multidimensional LSTMs for TensorFlow",
    long_description = long_description,
    # url = "https://github.com/pypa/sampleproject",
    author = "Thomas Breuel",
    author_email = "tbreuel@nvidia.com",
    license = "MIT",
    package_dir={"tfndlstm": "."},
    packages = ["tfndlstm"],
)
