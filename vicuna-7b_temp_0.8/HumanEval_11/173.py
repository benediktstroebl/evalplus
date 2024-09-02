from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    c = ''
    count = 0
    while a and b:
        if a[count] == '1':
            c += '0'
        else:
            c += '1'
        count += 1
    if a:
        c += '0' * (len(a) - count)
    if b:
        c += '0' * (len(b) - count)
    return c
