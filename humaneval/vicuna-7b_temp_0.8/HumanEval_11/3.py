from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    c = ''
    i = 0
    while i < len(a) and i < len(b):
        if a[i] != b[i]:
            c = a[i] * 2 + b[i]
            i += 1
        else:
            c += a[i]
            i += 1
    return c * 2

