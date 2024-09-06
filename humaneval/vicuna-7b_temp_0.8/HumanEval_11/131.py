from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = len(a)
    d = [0] * (n + 1)
    d[0] = d[1] = d[2] = 1
    d[n//2] = d[n//2 + 1] = d[n//2 + 2] = 0
    result = ''
    for i in range(n):
        if d[i] != d[i + 1]:
            result = d[i] if d[i] != 0 else d[i + 1]
            for j in range(i, n):
                d[j] ^= d[i]
    return result

