from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    if len(a) != len(b):
        raise ValueError("Inputs have different lengths")
    for i in range(len(a)):
        x = (int(a[i]) + int(b[i])) % 2
        result += str(x)
    return result

