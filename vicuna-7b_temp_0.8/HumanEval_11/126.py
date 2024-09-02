from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = len(str(a).split()) - len(str(b).split())
    b_zeros = len(str(b).split()) - len(str(a).split())
    return str(int(a_ones ^ b_zeros, 2))

