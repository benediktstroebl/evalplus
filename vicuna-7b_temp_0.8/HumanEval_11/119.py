from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = map(list, [int(s, 2) for s in (a, b)])
    return ''.join(str(x ^ y) for x, y in zip(a, b))

