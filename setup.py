import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daviddlima",
    version="0.0.1",
    author="David D'lima",
    author_email="david.dlima@tuta.io",
    description="Track and analyze personal fitness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daviddlima/fitness",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)