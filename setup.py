import setuptools
import os.path

from wireguard import __version__


DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(DIR, "README.md"), "r") as fh:
    long_description = fh.read()

# Info on arguments can be found at:
#   https://docs.python.org/3/distutils/apiref.html#distutils.core.setup
#   https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords
#   https://cffi.readthedocs.io/en/latest/cdef.html
setuptools.setup(
    name="wireguard",
    version=__version__,
    author="Andrew Roth",
    author_email="andrew@andrewjroth.com",
    description="Cross-platform userspace tooling for using and configuring WireGuard tunnels from Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewjroth/wireguard-python",
    packages=['wireguard'],
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: System :: Networking",
    ],
    python_requires='>=3.2',
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["wireguard_extension_build.py:ffibuilder"],
)
