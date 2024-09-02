from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return a[i] + b[i]
    return '0' * (len(a) + len(b))

