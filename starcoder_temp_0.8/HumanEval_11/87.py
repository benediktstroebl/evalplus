from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise Exception(f"strings should be of same length {a} and {b}")
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

