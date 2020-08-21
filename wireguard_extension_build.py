# Based on: https://cffi.readthedocs.io/en/latest/overview.html
from cffi import FFI
import os.path


DIR = os.path.abspath(os.path.dirname(__file__))

ffibuilder = FFI()

ffibuilder.set_source("_wireguard",
"""
    #include "wireguard.h"
""",
    include_dirs=[os.path.join(DIR, "wireguard-tools/contrib/embeddable-wg-library")],
    sources=['wireguard.c'],
    libraries=['net/if']
    )

ffibuilder.cdef("typedef uint8_t wg_key[32];")
ffibuilder.cdef("void wg_generate_preshared_key(wg_key preshared_key);")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

