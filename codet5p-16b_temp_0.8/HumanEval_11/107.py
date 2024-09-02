from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a)!= len(b):
        raise ValueError('Input strings must be the same length.')

    result = []

    for index in range(len(a)):
        a_char = int(a[index])
        b_char = int(b[index])

        result.append(str(a_char ^ b_char))

    return ''.join(result)

