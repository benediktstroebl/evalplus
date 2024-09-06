from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_bin = bin(int(a, 2))[2:]
    b_bin = bin(int(b, 2))[2:]
    if len(a_bin) > len(b_bin):
        b_bin = '0' * (len(a_bin) - len(b_bin)) + b_bin
    elif len(a_bin) < len(b_bin):
        a_bin = '0' * (len(b_bin) - len(a_bin)) + a_bin
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(a_bin, b_bin))
    
