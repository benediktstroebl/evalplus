from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bin = int(a, 2)
    b_bin = int(b, 2)
    result = bin(a_bin ^ b_bin)[2:]
    return result.zfill(max(len(a), len(b)))

