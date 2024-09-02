from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    a_ind = 0
    b_ind = 0
    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] == b[b_ind]:
            a_ind += 1
            b_ind += 1
        else:
            result += a[a_ind]
            a_ind += 1
            b_ind = b_ind + 1
    return result + string_xor(a[a_ind:], b[b_ind:])

