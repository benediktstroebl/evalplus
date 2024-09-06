from typing import List
def string_xor(a: str, b: str) -> str:
    return '__'.join(c^b for c in a for b in '01')