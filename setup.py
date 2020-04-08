#!/usr/bin/env python3
import os
import sys

import setuptools.command.egg_info as egg_info_cmd
from setuptools import setup

SETUP_DIR = os.path.dirname(__file__)
README = os.path.join(SETUP_DIR, "README.md")

try:
    import gittaggers

    tagger = gittaggers.EggInfoFromGit
except ImportError:
    tagger = egg_info_cmd.egg_info

install_requires = ["flask", "bh20-seq-uploader @ git+https://github.com/arvados/bh20-seq-resource@master"]

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest < 6", "pytest-runner < 5"] if needs_pytest else []

setup(
    name="bh20-simple-web-uploader",
    version="1.0",
    description="Biohackathon sequence uploader",
    long_description=open(README).read(),
    long_description_content_type="text/markdown",
    author="Adam Novak",
    author_email="anovak@soe.ucsc.edu",
    license="Apache 2.0",
    packages=["bh20simplewebuploader"],
    install_requires=install_requires,
    setup_requires=[] + pytest_runner,
    tests_require=["pytest<5"],
    zip_safe=True,
    cmdclass={"egg_info": tagger},
    python_requires=">=3.5, <4",
)
