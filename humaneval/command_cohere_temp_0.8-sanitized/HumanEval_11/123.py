from typing import List
def string_xor(a: str, b: str) -> str:
    return '__'.join(char ^ b for char in a for x, char in enumerate(a) if x ^ b)