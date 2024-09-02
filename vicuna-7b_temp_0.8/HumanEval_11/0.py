from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = [int(x) for x in a.split('')]
    b_list = [int(x) for x in b.split('')]
    a_not_b = [x for x in a_list if x != int(b_list[x])]
    b_not_a = [x for x in b_list if x != int(a_list[x])]
    result = ''.join([x for x in a_not_b if x != '0' and x != '1'])
    return result

