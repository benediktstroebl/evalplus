from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) != len(b):
        raise Exception('Strings need to be of equal length')

    result = ''
    for idx, _ in enumerate(a):
        result += '1' if a[idx] != b[idx] else '0'

    return result

