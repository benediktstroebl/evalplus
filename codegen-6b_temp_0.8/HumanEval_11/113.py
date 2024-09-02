from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert each string to a list of bits
    a_list = list(map(int, format(int(a, 2), '0' + str(len(a)) + 'b')))
    b_list = list(map(int, format(int(b, 2), '0' + str(len(b)) + 'b')))
    # perform xor
    res_list = [x ^ y for x, y in zip(a_list, b_list)]
    # convert back to string
    return format(int(''.join(map(str, res_list)), 2), '0' + str(len(a)) + 'b')

