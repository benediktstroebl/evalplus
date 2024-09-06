from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_int = int(a, 2)
    b_int = int(b, 2)
    a_xor_b = a_int ^ b_int
    a_xor_b_string = '{0:b}'.format(a_xor_b)
    return a_xor_b_string

