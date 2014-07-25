#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def desc():
    info = read('README.md')
    try:
        return info + '\n\n' + read('HISTORY.md').replace('.. :changelog:', '')
    except IOError:
        return info


def reqs(*f):
    return [
        r for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]


file_text = read(fpath('arrow/__init__.py'))
install_requires = reqs('requirements.txt')


setup(
    name='arrow',
    version=grep('__version__'),
    author=grep('__author__'),
    author_email=grep('__email__'),
    license=grep('__license__'),
    description='Better dates and times for Python',
    url='http://crsmithdev.com/arrow',
    long_description=desc(),
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    test_suite="tests",
)










