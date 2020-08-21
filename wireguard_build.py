# Based on: https://cffi.readthedocs.io/en/latest/overview.html
from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_wireguard",
"""
    #include "wireguard.h"
""",
    sources=['wireguard.c']
    )

ffibuilder.cdef("void wg_generate_preshared_key(wg_key preshared_key);");

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

