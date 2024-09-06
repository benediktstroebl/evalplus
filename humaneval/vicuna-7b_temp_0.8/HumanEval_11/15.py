from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    count = 0
    result = ''
    for x in a:
        if x == '0':
            count += 1
        else:
            count -= 1
    for y in b:
        if y == '0':
            count += 1
        else:
            count -= 1
    if count % 2 != 0:
        return '0'
    else:
        return '1'

