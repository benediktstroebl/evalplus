from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_binary = a.replace('0', '1').replace('1', '0')
    b_binary = b.replace('0', '1').replace('1', '0')
    binary_result = ''
    for i in range(max(len(a_binary), len(b_binary))):
        a_bit = a_binary[i] if i < len(a_binary) else '0'
        b_bit = b_binary[i] if i < len(b_binary) else '0'
        if a_bit == b_bit:
            binary_result += '0'
        else:
            binary_result += '1'
    return binary_result

