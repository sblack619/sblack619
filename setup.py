from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="SBLACK TEAM ",
    version="3.4.0",
    description="Exploitation Framework for Embedded Devices",
    long_description=long_description,
    author="MR KING / SENPAI / HTLER / SA3F / MILANO ",
    COMMUNITY : "THE BLACK SQUAD"
    packages=find_packages(),
    include_package_data=True,
    scripts=('rsf.py',),
    entry_points={},
    install_requires=[
        "future",
        "requests",
        "paramiko",
        "pysnmp",
        "pycryptodome",
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
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
)
