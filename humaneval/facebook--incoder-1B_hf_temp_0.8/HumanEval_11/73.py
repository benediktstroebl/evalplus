from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bin = bin(ord(a))[2:]
    b_bin = bin(ord(b))[2:]
    return b_bin[0] ^ a_bin[0]

