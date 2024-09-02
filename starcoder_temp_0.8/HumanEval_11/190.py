from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError('Arguments to XOR must be of equal length.')

    return "".join(map(lambda x, y: '0' if x == y else '1', a, b))

