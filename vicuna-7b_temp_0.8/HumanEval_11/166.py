from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    count = 0
    result = ''
    for char1, char2 in zip(a, b):
        if char1 == '1':
            count += 1
            if char2 == '1':
                count += 1
                if count == 2:
                    result += '1'
                elif count == 1:
                    result += '0'
                count = 0
        else:
            count = 0
    if count > 0:
        result += '1'
    return result

