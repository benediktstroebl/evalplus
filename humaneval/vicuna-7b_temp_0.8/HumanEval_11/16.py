from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = max(len(a), len(b))
    c = ''
    for i in range(n):
        xor = a[i] != b[i]
        c += str(xor).rjust(2, '0') if i < len(a) else str(~xor).rjust(2, '0')
    return c

