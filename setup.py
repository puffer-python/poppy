import os

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(HERE, 'README.md'), 'r', encoding='utf8').read()
setup(
    name='poppy_python',
    version='1.0.0',
    description='A Poppy Python package',
    long_description=long_description,
    author='Dung BV',
    author_email='bvdzung@gmail.com',
    packages=['poppy_python'],
    install_requires=[
        'pytz', 'slugify'
    ],
)
