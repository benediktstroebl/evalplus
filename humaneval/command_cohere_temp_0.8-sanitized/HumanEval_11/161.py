def string_xor(a, b):
    return bytes(a.encode()).xor(bytes(b.encode())).decode()