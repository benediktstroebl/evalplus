from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not (len(a) == len(b)):
        raise ValueError
    a_bin = bin(int(a, 2))[2:]
    b_bin = bin(int(b, 2))[2:]
    if len(a_bin) < len(b_bin):
        a_bin = "0" * (len(b_bin) - len(a_bin)) + a_bin
    elif len(a_bin) > len(b_bin):
        b_bin = "0" * (len(a_bin) - len(b_bin)) + b_bin
    result = "".join(str(int(x) ^ int(y)) for x, y in zip(a_bin, b_bin))
    return result

