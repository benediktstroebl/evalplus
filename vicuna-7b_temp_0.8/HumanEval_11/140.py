from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert binary strings to integer and perform XOR
    ai = sum(int(c) for c in a) ^ sum(int(c) for c in b)
    bi = sum(int(c) for c in b) ^ sum(int(c) for c in a)
    # Convert integer to string
    return str(ai) + str(bi)
