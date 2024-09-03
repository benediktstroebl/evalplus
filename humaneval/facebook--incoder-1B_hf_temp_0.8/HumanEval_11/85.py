from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not a or not b:
        return b
    result = ""
    for i in range(0, len(a)):
        if a[i]!= b[i]:
            result += "1"
        else:
            result += "0"
    return result

