from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Cast each character of the string to int
    a_list = list(map(int, a))
    b_list = list(map(int, b))
    xor_result = [str(i ^ j) for i, j in zip(a_list, b_list)]
    return ''.join(xor_result)

