from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_num = int(a)
    b_num = int(a)
    a_str_ = bin(a_num)[2:]
    b_str_ = bin(b_num)[2:]
    a_str_ = a_str_[0] + a_str_[1]
    b_str_ = b_str_[0] + b_str_[1]
    return a_str_ ^ b_str_

