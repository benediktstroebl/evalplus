from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert a!= b
    assert len(a) == len(b)
    xor = 0
    for i in range(len(a)):
        xor = (xor << 1) | (ord(a[i]) ^ ord(b[i]))
    return chr(xor
