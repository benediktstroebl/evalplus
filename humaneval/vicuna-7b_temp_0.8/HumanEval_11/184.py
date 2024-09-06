from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = a.split()
    b_list = b.split()
    a_set = set(a_list)
    b_set = set(b_list)
    return ''.join([str(x) for x in set(a_set) ^ set(b_set)])
