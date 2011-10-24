#!/usr/bin/env python

from distutils.core import setup

setup(name='lpbs',
      version='0.0.1',
      description='Local Portable Batch System',
      author='Michael Goerz',
      author_email='goerz@physik.uni-kassel.de',
      url='http://michaelgoerz.net',
      license='GPL',
      packages=['LPBS'],
      scripts=['lqsub']
     )