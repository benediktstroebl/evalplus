from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = list(map(''.join, (a, b)))
    if len(a) == 0 or len(b) == 0:
        return ''
    length = len(a)
    result = b * length
    for i in range(length):
        result ^= a[i * length + length]
    return list(result)

