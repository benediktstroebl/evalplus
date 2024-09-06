from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    result = ''
    for index in range(len(a)):
        a_bit = a[index]
        b_bit = b[index]
        xor_bit = a_bit!= b_bit
        result += str(xor_bit)
    return result

