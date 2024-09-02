from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = list(a)
    b_list = list(b)
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if a_list[i] == b_list[j] and a_list[i] != '0' and b_list[j] != '0':
                a_list[i], b_list[j] = '0', a_list[i] ^ b_list[j]
    return ''.join(a_list)

