from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if a is None or len(a) == 0 or b is None or len(b) == 0:
        return ''

    s = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            s += '0'
        else:
            s += '1'
    return s

