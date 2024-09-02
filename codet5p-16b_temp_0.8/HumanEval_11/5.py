from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError("Input strings must be of same length")
    res = ""
    for ai, bi in zip(a, b):
        res += '1' if int(ai) ^ int(bi) else '0'
    return res

