import codecs
import os

# To get the wheel build to work in python 3.7 Anaconda3 5.3.1 the follwing changes were made...
# Commented out the following line..
# from setuptools import setup, find_packages, Extension

# Added the following lines...
from setuptools import find_packages
from distutils.core import setup
# End changes

from src.pymovie import version

###################################################################

VERSION = version.version()

NAME = "pymovie"

PACKAGES = find_packages(where="src")

print("")
for pkg in PACKAGES:
    print('############## package found: ' + str(pkg))
print(f'{len(PACKAGES)} packages were found\n')

KEYWORDS = ["desktop app", "lightcurve extraction from astronomical videos"]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Scientific/Engineering",
]

# We don't put PyQt5 in the INSTALL_REQUIRES because we assume that the Anaconda distribution is
# in use, and that distribution has PyQt5 already installed.  Adding PyQt5 in this list also works, but adds about
# 100Mb to the normal install download of about 10Mb

INSTALL_REQUIRES = ['pyqtgraph', 'opencv-python', 'astroquery',
                    'scikit-image(>=0.15.0)',
                    'winshell;platform_system=="Windows"',
                    'pypiwin32;platform_system=="Windows"']

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


if __name__ == "__main__":
    setup(
        name=NAME,
        python_requires='>=3.7',
        description='pymovie is a lightcurve extractor for astronomical videos',
        license='License :: OSI Approved :: MIT License',
        url=r'https://github.com/bob-anderson-ok/pymovie',
        version=VERSION,
        author='Bob Anderson',
        author_email='bob.anderson.ok@gmail.com',
        maintainer='Bob Anderson',
        maintainer_email='bob.anderson.ok@gmail.com',
        keywords=KEYWORDS,
        long_description=read("README.rst"),
        packages=PACKAGES,
        package_dir={"": "src"},
        zip_safe=False,
        package_data={'': ['*.bat']},
        include_package_data=True,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )