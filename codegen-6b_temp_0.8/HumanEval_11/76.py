from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a, b = a.zfill(len(a)), b.zfill(len(b))
    result = ""
    for i in range(len(a)):
        if a[i] in '01' and b[i] in '01':
            result += '0'
        elif a[i] in '01' and b[i] in '10':
            result += '1'
        elif a[i] in '10' and b[i] in '01':
            result += '1'
        elif a[i] in '10' and b[i] in '10':
            result += '0'
    return result.lstrip('0')

