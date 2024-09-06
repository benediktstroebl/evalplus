from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_result = []
    for i, j in zip(a, b):
        if i == '0' and j == '0':
            xor_result.append('0')
        elif i == '0' and j == '1':
            xor_result.append('1')
        elif i == '1' and j == '0':
            xor_result.append('1')
        elif i == '1' and j == '1':
            xor_result.append('0')
    return "".join(xor_result)

