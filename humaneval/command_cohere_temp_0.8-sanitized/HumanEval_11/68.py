def string_xor(a, b):
    return bytes([c^b for c in a]).decode()