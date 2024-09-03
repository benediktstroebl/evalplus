from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_str = a.encode()
    b_str = b.encode()
    if len(a_str)!= len(b_str):
        raise ValueError(
            f"Inputs length mismatch {len(a_str)} vs {len(b_str)}"
        )
    result = ""
    for a, b in zip(a_str, b_str):
        result = chr(ord(a) ^ ord(b))
    return result

