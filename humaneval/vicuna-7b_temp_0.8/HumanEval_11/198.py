from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to integers
    a_int = sum(int(c) for c in a)
    b_int = sum(int(c) for c in b)
    # Perform XOR operation on integers
    result_int = a_int ^ b_int
    # Convert result to string
    result = str(result_int)
    return result
