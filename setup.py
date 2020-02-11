#!/usr/bin/env python


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the APAC package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##


import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

__version__ = '0.1.0'

setuptools.setup(
	name='apac',
	version=__version__,
	author='Kyoungseob Byeon',
	author_email='brec4u@gmail.com',
	description='Automatically parcellate putative human core using myelin content and curvature',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/Raon31/apac',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
		]
)