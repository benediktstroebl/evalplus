from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = 0
    for x in range(0, len(b)):
        result ^= ord(b[x]) * (ord(a[x]) - 1)
    return result

