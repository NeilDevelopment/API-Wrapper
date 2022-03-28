from setuptools import setup, find_packages
import codecs

VERSION = '0.0.3'
DESCRIPTION = 'A API wrapper for the Neil Development API'

setup(
    name="neildevapi",
    version=VERSION,
    author="Neil Development",
    author_email="<hello@neildevelopment.xyz>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)