from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_ones = [i if i == '1' else '' for i in a]
    b_ones = [i if i == '1' else '' for i in b]
    result = ''
    for i in range(len(a_ones)):
        for j in range(len(b_ones)):
            if a_ones[i] == '0' and b_ones[j] == '0':
                result += '0'
            elif a_ones[i] != b_ones[j]:
                result += a_ones[i]
                if j < len(b_ones) - 1:
                    result += '0'
                else:
                    result += '1'
        if i < len(a_ones) - 1:
            result += '0'
    return result

