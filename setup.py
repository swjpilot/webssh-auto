import codecs
from setuptools import setup
from webssh-auto._version import __version__ as version


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='webssh-auto',
    version=version,
    description='Web based ssh client',
    long_description=long_description,
    author='Scott John',
    author_email='scott@thejohnweb.com',
    url='https://github.com/swjpilot/webssh-auto',
    packages=['webssh-auto'],
    entry_points='''
    [console_scripts]
    wssh-auto = webssh-auto.main:main
    ''',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'tornado>=4.5.0',
        'paramiko>=2.3.1',
    ],
)
