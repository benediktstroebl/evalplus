from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bin = [int(i) for i in a]
    b_bin = [int(i) for i in b]

    result_bin = []

    for i in range(len(a_bin)):
        result_bin.append(a_bin[i] ^ b_bin[i])

    return ''.join(str(x) for x in result_bin)

