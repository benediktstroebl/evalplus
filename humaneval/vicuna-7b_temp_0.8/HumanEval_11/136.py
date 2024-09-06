from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    if a == '0':
        for i in range(len(b)):
            if b[i] == '0':
                result = '1' + result
            else:
                result = '0' + result
    else:
        for i in range(len(b)):
            if b[i] == '0':
                result = b[i] + result
            else:
                result = result + b[i]
    return result

