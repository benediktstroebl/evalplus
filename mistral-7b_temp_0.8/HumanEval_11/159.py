from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    res = ''
    for x, y in zip(a, b):
        if x == y:
            res += '0'
        else:
            res += '1'
    return res

