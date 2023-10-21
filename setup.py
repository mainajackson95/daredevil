from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()
setup(
    name="DAREDEVIL",
    version="1",
    description="Web Application Security Scanner",
    long_description=long_description,
    author="s0md3v",
    url="https://github.com/s0md3v",
    download_url="https://github.com/s0md3v/XSStrike/DAREDEVIL",
    packages=find_packages(),
    include_package_data=True,
    scripts=('DAREDEVIL',),
    entry_points={},
    install_requires=[
        "requests",
    ],
    extras_require={
        "tests": [
            "pytest",
            "pytest-forked",
            "pytest-xdist",
            "flake8",
        ],
    },
    classifiers=[
        "Operating System :: POSIX",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Security",
        "Topic :: System :: Web",
        "Topic :: Utilities",
    ],
)
