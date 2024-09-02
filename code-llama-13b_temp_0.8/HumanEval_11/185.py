from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # if a and b are empty string
    if not a and not b:
        return ""
    # if a or b is empty string
    if not a or not b:
        return "1" * max(len(a), len(b))
    # if a and b are not empty string
    return str(int(a, 2) ^ int(b, 2))

