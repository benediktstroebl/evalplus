from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert (len(a) == len(b))
    a_list = list(a)
    b_list = list(b)
    for i in range(len(a_list)):
        if a_list[i]!= b_list[i]:
            a_list[i] = '1' if a_list[i] == '0' else '0'
            b_list[i] = '1' if b_list[i] == '0' else '0'
    return ''.join(a_list)

