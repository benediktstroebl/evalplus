from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError("Strings should have the same length")

    result = ""
    for a_, b_ in zip(a, b):
        result += str(int(a_) ^ int(b_))

    return result

