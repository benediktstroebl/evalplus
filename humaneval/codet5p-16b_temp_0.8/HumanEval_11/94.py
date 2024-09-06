from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) > len(b):
        return string_xor(b, a)

    res = [a[i] == '1' and b[i] == '1' for i in range(len(a))]
    return ''.join(['1' if x else '0' for x in res])

