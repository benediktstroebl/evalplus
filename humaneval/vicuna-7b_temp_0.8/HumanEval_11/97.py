from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_count = 0
    b_count = 0
    result = ""
    for char in a:
        if char == "0":
            a_count += 1
        else:
            b_count += 1
    for char in b:
        if char == "0":
            b_count += 1
        else:
            a_count += 1
    if a_count == b_count:
        result = "0"
    else:
        result = "1"
    return result

