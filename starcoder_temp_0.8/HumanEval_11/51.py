from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError('Input strings should be of equal length')

    a_int = int(a, 2)
    b_int = int(b, 2)
    xor_int = a_int ^ b_int
    xor_string = bin(xor_int)[2:]

    return xor_string

