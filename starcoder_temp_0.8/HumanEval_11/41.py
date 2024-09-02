from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError("Lengths of a and b are not equal")

    result = ''
    for i in range(len(a)):
        if a[i] == '0' and b[i] == '0':
            result = result + '0'
        elif a[i] == '0' and b[i] == '1':
            result = result + '1'
        elif a[i] == '1' and b[i] == '0':
            result = result + '1'
        else:
            result = result + '0'

    return result

