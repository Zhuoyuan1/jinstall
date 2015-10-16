#!/usr/bin/env python

from setuptools import setup

setup(
        name='jinstall',
        version='0.2',
        install_requires=['urwid'],
        description='A terminal-based automated file installer',
        author='Joël Porquet',
        author_email='joel@porquet.org',
        url='https://joel.porquet.org/wiki/hacking/jinstall/',
        scripts=['jinstall'],
        license='GPLv3'
        )

