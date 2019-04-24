import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfwatermark-mvartanyan",
    version="0.0.1",
    author="Michael Vartanyan",
    author_email="mickiedesman@gmail.com",
    description="A utility to watermark PDF files with "
                "custom text using command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mvartanyan/pdfwatermark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
