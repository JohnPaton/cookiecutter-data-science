from os.path import dirname, basename, isfile, join
from setuptools import find_packages
import glob

# find all python modules in this file's directory
modules = glob.glob(join(dirname(__file__), "*.py"))

# find any subpackages in directory
subpackages = find_packages()

# automatically import modules
__all__ = [
    basename(f)[:-3]  # drop ".py"
    for f in modules 
    if isfile(f) 
    and not f.endswith('__init__.py')  # exclude this file
]

# automatically import subpackages
__all__ += subpackages
