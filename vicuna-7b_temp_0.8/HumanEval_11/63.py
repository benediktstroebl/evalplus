from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n1, n2 = len(a), len(b)
    result = ''
    for i in range(n1):
        for j in range(n2):
            if a[i] == '1' and b[j] == '1':
                result += '1'
            else:
                result += '0'
    return result

