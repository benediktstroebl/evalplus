from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [1 if c == '1' else 0 for c in a]
    a_zeros = [0 if c == '1' else 1 for c in a]
    b_ones = [1 if c == '1' else 0 for c in b]
    b_zeros = [0 if c == '1' else 1 for c in b]
    result = ''.join([a_ones[i] ^ b_ones[i] for i in range(len(a_ones))])
    return result
