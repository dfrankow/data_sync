import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read_requirements():
    current = os.path.dirname(os.path.realpath(__file__))
    requirement_path = current + '/requirements.txt'
    install_requires = []
    if os.path.isfile(requirement_path):
        with open(requirement_path) as f:
            install_requires = f.read().splitlines()
    return install_requires


setuptools.setup(
    name="reldatasync",
    version="0.0.1",
    author="Dan Frankowski",
    author_email="dfrankow+rds@gmail.com",
    description="Synchronize relational data between two entities",
    install_requires=read_requirements(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dfrankow/data_sync",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    test_suite='nose.collector',
    tests_require=['nose'],
)
