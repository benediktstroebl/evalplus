from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert len(a) == len(b) == 2 ** binary_size(a) == binary_size(b)
    xor_bytes = [a_bit ^ b_bit for a_bit, b_bit in zip(a, b)]
    return ''.join(map(str, xor_bytes))

