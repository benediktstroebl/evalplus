from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Runs in linear time with respect to the length of the input
    a_as_binary = int(a, 2)
    b_as_binary = int(b, 2)
    xor_value = a_as_binary ^ b_as_binary
    return bin(xor_value)[2:]

