from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    count = 0
    for char in a:
        if char == "0":
            result += "1"
            count += 1
        else:
            result += "0"
            count += 1
    result = result[::-1]
    result += str(count) + b
    return result[::-1]

