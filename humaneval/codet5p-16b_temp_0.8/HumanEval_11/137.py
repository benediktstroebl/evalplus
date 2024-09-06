from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError("Input strings should be equal length")

    result = []

    for ai, bi in zip(a, b):
        result.append(str(int(ai) ^ int(bi)))

    return "".join(result)

