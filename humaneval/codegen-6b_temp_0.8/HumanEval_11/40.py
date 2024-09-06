from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    l = []
    for i in range(1, len(a)):
        if a[i] == b[i]:
            l.append('0')
        else:
            l.append('1')
    return ''.join(l)

