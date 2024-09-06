from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [1 if c == '0' else 0 for c in a]
    b_ones = [1 if c == '0' else 0 for c in b]
    a_zeros = [0 if c == '1' else 1 for c in a]
    b_zeros = [0 if c == '1' else 1 for c in b]
    result = ''
    for i in range(len(a_ones), len(a_ones) + len(b_ones)):
        result += str(a_ones[i-len(b_ones):i])
    for i in range(len(b_ones), len(a)):
        result += str(b_ones[i-len(a_ones):i])
    return result

