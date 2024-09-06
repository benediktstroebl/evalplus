from typing import List
def string_xor(a: str, b: str) -> str:
    return bytes.fromhex(a.translate(str.maketrans('01', '10')) ^ b.translate(str.maketrans('01', '10')))[0].decode()