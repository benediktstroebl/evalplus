from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = a.zfill(2)
    b = b.zfill(2)
    xor = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            xor |= 1 << (len(a) - i - 1)
    return xor.zfill(2)

