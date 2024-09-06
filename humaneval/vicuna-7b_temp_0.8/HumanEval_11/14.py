from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Perform binary XOR on a and b
    xor_result = 0
    for i in range(len(a)):
        if a[i] == '1':
            xor_result ^= b[i]
        elif b[i] == '1':
            xor_result ^= a[i]
    return '1' if xor_result == 0 else '0'

