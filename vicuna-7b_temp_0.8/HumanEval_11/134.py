from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_mask = '0'
    b_mask = '0'
    a_ones = '1'
    b_ones = '1'
    result = ''
    for i in range(len(a)):
        if a[i] == '1':
            a_mask = a_mask[:i] + '0' + a_mask[i+1:]
            a_ones = a_ones[:i] + '0' + a_ones[i+1:]
        result = a_ones + result
        if b[i] == '1':
            b_mask = b_mask[:i] + '0' + b_mask[i+1:]
            b_ones = b_ones[:i] + '0' + b_ones[i+1:]
        result = b_ones + result
    return a_mask + result

