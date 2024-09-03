from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if a[:1]!= '0' or b[:1]!= '1':
        raise ValueError('string_xor: Invalid arguments')
    return bin(a[0])^bin(b[0])

