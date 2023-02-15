from setuptools import setup

setup(
    name='poppy',
    version='1.0.0',
    description='A Poppy Python package',
    author='Dung BV',
    author_email='bvdzung@gmail.com',
    packages=['poppy'],
    install_requires=[
        'pytz', 'slugify'
    ],
)
