from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_bin = bin(int(a, 2))[2:]
    b_bin = bin(int(b, 2))[2:]
    result = ""
    for i in range(len(a_bin)):
        if int(a_bin[i]) ^ int(b_bin[i]) == 1:
            result += '1'
        else:
            result += '0'
    return result

