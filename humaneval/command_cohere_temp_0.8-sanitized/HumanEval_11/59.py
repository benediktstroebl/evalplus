from typing import List
def string_xor(a: str, b: str) -> str:
    return str(int(a, 2) ^ int(b, 2))