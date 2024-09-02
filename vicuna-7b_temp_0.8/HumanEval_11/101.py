from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [i == '1' for i in a]
    a_zeros = [i == '0' for i in a]
    b_ones = [i == '1' for i in b]
    b_zeros = [i == '0' for i in b]

    # Perform XOR on corresponding elements of a and b
    result = ''
    for i in range(len(a_ones)):
        if a_ones[i] != b_ones[i]:
            result += '1'
        else:
            result += '0'
    for i in range(len(a_zeros)):
        if a_zeros[i] != b_zeros[i]:
            result += '1'
        else:
            result += '0'

    return result
