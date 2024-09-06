from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    c, d = 0, 0
    for i in range(len(a)):
        if a[i] == '1':
            c += int(b[i])
        else:
            d += int(b[i])
    return str(c^d)

