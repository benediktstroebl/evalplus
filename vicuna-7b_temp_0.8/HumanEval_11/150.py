from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = {x for x in a}
    b_set = {x for x in b}
    return ''.join(set(a_set) ^ set(b_set))

