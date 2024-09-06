from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # length of both strings should be the same
    if len(a) != len(b):
        raise ValueError('a and b must have the same length')

    # XOR works on bits not on string characters
    # we need to convert string characters to bits
    def str_to_bit(x: str) -> str:
        return '0' if x == '0' else '1'

    res = ''
    for i in range(len(a)):
        res += str(int(str_to_bit(a[i]) != str_to_bit(b[i])))

    return res

