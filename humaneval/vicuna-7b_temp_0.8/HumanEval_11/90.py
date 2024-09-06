from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = set(a)
    b_set = set(b)
    a_set_diff = a_set - b_set
    b_set_diff = b_set - a_set
    return ''.join(['1' if x in a_set_diff else '0' for x in b_set_diff])

