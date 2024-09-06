from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("The length of both inputs should be the same")
    if not a.isdigit() or not b.isdigit():
        raise ValueError("Inputs should only consist of 1s and 0s")

    result = ""
    for (x, y) in zip(a, b):
        if x == y:
            result += "0"
        else:
            result += "1"

    return result

