#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.0.1',
    author="Pratik Karki",
    author_email='prertik@outlook.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['click', 'tinydb', 'six', 'pytest', 'pytest-mock'],
    tests_require=['pytest', 'pytest-mock'],
    extras_require={'mongo': 'pymongo'},
    entry_points={'console_scripts': [
        'tasks = tasks.cli:tasks_cli',
    ]},
)
