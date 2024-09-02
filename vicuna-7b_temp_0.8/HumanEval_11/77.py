from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integer using bin conversion
    a_int = sum(int(c) for c in a)
    b_int = sum(int(c) for c in b)
    # Perform XOR operation on the converted integers
    xor_int = a_int ^ b_int
    # Convert the integer back to a string using the same code as above
    xor_str = str(xor_int)
    return xor_str
