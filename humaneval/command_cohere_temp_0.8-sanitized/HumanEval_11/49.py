from typing import List
def string_xor(a: str, b: str) -> str:
    return '__'.join(ch1 ^ ch2 for ch1, ch2 in zip(a, b))