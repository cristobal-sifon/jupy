from __future__ import absolute_import, division, print_function


import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# folder where `jupy` is stored
here = os.path.abspath(os.path.dirname(__file__))

#this function copied from pip's setup.py
#https://github.com/pypa/pip/blob/1.5.6/setup.py
#so that the version is only set in the __init__.py and then read here
#to be consistent
def find_version(fname):
    version_file = read(fname)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


#Taken from the Python docs:
#Utility function to read the README file.
#Used for the long_description.  It's nice, because now 1) we have a
#top level README file and 2) it's easier to type in the README file
#than to put a raw string in below
def read(fname):
    return open(os.path.join(here, fname)).read()


"""
setup(
    name='jupy',
    #version=find_version('jupy/__init__.py'),
    description='Common IPython notebook settings utility',
    author='Cristobal Sifon',
    author_email='sifon@astro.princeton.edu',
    long_description=read('README.md'),
    url='https://github.com/cristobal-sifon/jupy',
    packages=['jupy'],
    zip_safe=False
)
"""

msg = """

No installation required. Please add the following line to your `~/.bashrc` 
or `~/.bash_profile`:

    export jupy={0}

or to your `~/.cshrc`, `~/.tcshrc`, etc:

    setenv jupy {0}
""".format(here)
print(msg)
