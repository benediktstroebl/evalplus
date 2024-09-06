from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a = bin(int(a))[2:]  # convert to binary and remove 0b prefix
    b = bin(int(b))[2:]  # convert to binary and remove 0b prefix
    if len(a) < len(b):
        a = (len(b) - len(a)) * '0' + a  # pad a with zeros
    else:
        b = (len(a) - len(b)) * '0' + b  # pad b with zeros
    result = ''
    carry = 0
    for i in range(1, len(a) + 1):
        if int(a[-i]) ^ int(b[-i]) ^ carry == 1:
            result += '1'
            carry = 0
        else:
            result += '0'
            carry = 1
    if carry == 1:
        result += '1'
    return result[::-1]

