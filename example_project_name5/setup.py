#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Anna Chernova",
    author_email='karloanna8617@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is an example project to show off how cookiecutter works",
    entry_points={
        'console_scripts': [
            'example_project_name5=example_project_name5.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='example_project_name5',
    name='example_project_name5',
    packages=find_packages(include=['example_project_name5', 'example_project_name5.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ann-chern/example_project_name5',
    version='0.1.0',
    zip_safe=False,
)
