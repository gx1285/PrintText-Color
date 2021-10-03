import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color-printtext",
    version="0.1",
    author="gx1285",
    author_email="runay2342@gmail.com",
    description="PrintColor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gx1285/Print-Color",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
