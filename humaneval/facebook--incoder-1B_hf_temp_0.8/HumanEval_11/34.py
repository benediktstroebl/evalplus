from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    bina = bin(a)[2:]
    binb = bin(b)[2:]
    return ''.join([a ^ b for a, b in zip(bina, binb) if len(a)!= len(b)])

