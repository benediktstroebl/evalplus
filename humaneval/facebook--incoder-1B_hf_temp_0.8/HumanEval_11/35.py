from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("a and b must be same length")

    result = ''
    for x in range(len(a)):
        result += (1 if a ^ b[x] == 0 else 0)

    return result

