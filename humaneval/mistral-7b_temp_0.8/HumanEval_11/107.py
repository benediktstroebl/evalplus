from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError('Input strings should be of same length')
    a = list(a)
    b = list(b)
    for i, (x, y) in enumerate(zip(a, b)):
        if x == '1' and y == '1':
            a[i] = '0'
        elif x == '0' and y == '0':
            a[i] = '1'
        else:
            a[i] = '1'
    return ''.join(a)

