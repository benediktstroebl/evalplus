from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = map(list, [x.split('') for x in (a, b)])
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                return a[i] * b[j]
    return '0' * (len(a) + len(b))

