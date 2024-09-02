from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to binary numbers
    a_bin = bin(int(a, 2))
    b_bin = bin(int(b, 2))

    # Perform binary XOR
    xor_bin = bin(int(a_bin ^ b_bin, 2))

    # Convert binary number to string and return result
    return bin(int(xor_bin, 2))

