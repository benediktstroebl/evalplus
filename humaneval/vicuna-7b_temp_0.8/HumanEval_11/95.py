from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_0_count = 0
    b_0_count = 0
    result_count = 0
    for i in range(len(a)):
        if a[i] == '0':
            a_0_count += 1
        else:
            b_0_count += 1
    for i in range(len(b)):
        if b[i] == '0':
            b_0_count += 1
        else:
            result_count += 1
    if a_0_count == b_0_count:
        return '0' * result_count
    else:
        return '1' * (len(b) - result_count)

