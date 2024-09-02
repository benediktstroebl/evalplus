from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert a and b to list of 1s and 0s
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]

    # perform binary XOR on corresponding elements of a and b lists
    for i in range(len(a_list)):
        a_list[i] ^= b_list[i]

    # convert list of 1s and 0s back to a string
    return ''.join(str(x) for x in a_list)
