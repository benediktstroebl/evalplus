from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = list(a)
    b_list = list(b)
    if len(a_list) > len(b_list):
        b_list.extend([0] * (len(a_list) - len(b_list)))
    else:
        a_list.extend([0] * (len(b_list) - len(a_list)))
    result = []
    for i in range(len(a_list)):
        result.append(str(int(a_list[i]) ^ int(b_list[i])))
    return "".join(result)

