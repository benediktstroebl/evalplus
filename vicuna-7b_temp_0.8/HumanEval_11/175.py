from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if length of inputs are not same
    if len(a) != len(b):
        return '0'

    # Convert inputs to list and perform XOR
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]
    xor_list = list(set(a_list) ^ set(b_list))

    # Convert list to string
    xor_string = ''.join([str(x) for x in xor_list])

    return xor_string
