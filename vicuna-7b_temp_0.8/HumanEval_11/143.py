from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [i in str(a) for i in range(len(a))]
    b_ones = [i in str(b) for i in range(len(b))]
    a_zeros = [i not in str(a) for i in range(len(a))]
    b_zeros = [i not in str(b) for i in range(len(b))]
    if all(a_ones) and all(b_ones):
        return '1'
    elif all(a_zeros) and all(b_zeros):
        return '0'
    elif any(a_ones) and any(b_ones):
        c = '0'
        for i in range(len(a)):
            if a_ones[i] == b_ones[i]:
                c += str(a[i])
        return c
    elif any(a_zeros) and any(b_zeros):
        d = '0'
        for i in range(len(b)):
            if b_ones[i] == a_ones[i]:
                d += str(b[i])
        return d
    else:
        return '1'

