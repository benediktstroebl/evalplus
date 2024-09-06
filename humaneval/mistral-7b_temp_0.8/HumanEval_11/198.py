from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Your Code Here
    if a == '0' and b == '0':
        return '0'
    elif a == '0' and b == '1':
        return '1'
    elif a == '1' and b == '1':
        return '0'

    if a == '0':
        return string_xor('1', b)
    elif b == '0':
        return string_xor(a, '1')

    return string_xor(a[0: -1], b[0: -1])

