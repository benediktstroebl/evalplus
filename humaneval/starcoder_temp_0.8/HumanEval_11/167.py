from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # XOR on binary representation is just addition modulo 2.
    # Since we have str, we need to convert to int first.
    # Python ternary operator is amazing!
    return ''.join([str((int(a_bit) + int(b_bit)) % 2) for a_bit, b_bit in zip(a, b)])

