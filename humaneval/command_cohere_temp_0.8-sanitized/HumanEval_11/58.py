from typing import List
def string_xor(a: str, b: str) -> str:
    return '__'.join(x ^ y for x, y in zip(a, b))