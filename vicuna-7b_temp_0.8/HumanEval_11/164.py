from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_mask = '0'
    b_mask = '0'
    res_mask = '0'
    i = 0
    while i < min(len(a), len(b)):
        if a[i] == b[i]:
            a_mask = a_mask[:i] + a_mask[i+1:]
            b_mask = b_mask[:i] + b_mask[i+1:]
            i += 1
        elif a[i] == '1':
            res_mask = res_mask + '1'
        else:
            res_mask = res_mask + a_mask
    return res_mask

