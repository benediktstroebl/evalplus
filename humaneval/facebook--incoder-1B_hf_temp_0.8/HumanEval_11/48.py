from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xors = bin(int(a))[2:].zfill(32)
    xors += bin(int(b))[2:].zfill(32)
    return ''.join(xors)

