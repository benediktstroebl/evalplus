from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert inputs to list of 1s and 0s
    a_list = list(a)
    b_list = list(b)

    # Check for 1000 (all 1s) or 0111 (all 0s)
    if a_list == b_list:
        return '0'
    elif a_list == '0' * len(b_list):
        return '1' + b_list
    else:
        return '0' + a_list

