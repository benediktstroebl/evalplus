from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert inputs to binary
    a_binary = bin(int(a, 2))
    b_binary = bin(int(b, 2))

    # Convert binary to int
    a_int = int(a_binary, 2)
    b_int = int(b_binary, 2)

    # Perform xor
    a_b_xor = a_int ^ b_int

    # Convert xor result to binary
    a_b_xor_binary = bin(a_b_xor)

    # Convert binary to string
    return str(a_b_xor_binary)

