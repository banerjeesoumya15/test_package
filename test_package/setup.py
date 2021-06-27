
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'test_package'
AUTHOR = 'Soumya'
AUTHOR_EMAIL = 'banerjeesoumya15@gmail.com.com'
URL = 'https://github.com/banerjeesoumya15/test_package'

#LICENSE = 'Apache License 2.0'
LICENSE = 'MIT License'
DESCRIPTION = 'Describe your package in one sentence'
#LONG_DESCRIPTION = (HERE / "README.md").read_text()
#LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
