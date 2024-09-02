from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [int(x) for x in a if x == '1']
    b_ones = [int(x) for x in b if x == '1']
    a_zeros = [x for x in a if x == '0']
    b_zeros = [x for x in b if x == '0']
    return ''.join(['1' if a_one ^ b_one == 1 else '0' for a_one in a_ones for b_one in b_ones])

