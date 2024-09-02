from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) == 0 or len(b) == 0:
        return ''

    if a[0] == '0' and b[0] == '0':
        return '0' + string_xor(a[1:], b[1:])

    if a[0] == '1' and b[0] == '1':
        return '1' + string_xor(a[1:], b[1:])

    return '0' + string_xor(a[1:], b[1:])

