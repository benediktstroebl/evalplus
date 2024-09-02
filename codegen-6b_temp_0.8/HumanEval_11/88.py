from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # get the number values of the inputs string
    a, b = (int(a, 2), int(b, 2))
    return "{0:b}".format(a ^ b).zfill(max(len(a), len(b)))

