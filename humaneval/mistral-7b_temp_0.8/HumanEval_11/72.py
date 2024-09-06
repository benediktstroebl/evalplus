from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_lst = list(a)
    b_lst = list(b)

    if len(a_lst) != len(b_lst):
        raise ValueError("Strings of different length")

    result = ''
    for i in range(len(a_lst)):
        result += str(int(a_lst[i]) ^ int(b_lst[i]))

    return result

