from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_one = '0' if a.startswith('0') else '1'
    b_one = '0' if b.startswith('0') else '1'
    result = ''
    for i in range(len(a)):
        result = a_one[i] + result + b_one[i]
    return result

