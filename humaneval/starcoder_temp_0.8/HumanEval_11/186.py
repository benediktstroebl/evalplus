from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert(len(a) == len(b))
    s_xor = ''
    for a_i, b_i in zip(a, b):
        if a_i == b_i:
            s_xor += '0'
        else:
            s_xor += '1'
    return s_xor

