from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = bin(ord(a[0]) & 0b111) + bin(ord(a[1]) & 0b111)
    b_set = bin(ord(b[0]) & 0b111) + bin(ord(b[1]) & 0b111)
    return str((ord(a[0]) ^ ord(b[0])) ^ ord(a[1]) ^ ord(b[1]))

