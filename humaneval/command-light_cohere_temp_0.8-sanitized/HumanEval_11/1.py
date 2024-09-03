from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two input strings a and b and return result as a string."""
    if not a or not b:
        raise ValueError("Both inputs cannot be empty")
    return "".join([c ^ d for c, d in ('0', '1')])  # XOR between digits returns digit 0 or 1