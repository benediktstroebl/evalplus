from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    a_bits = a.replace('0', '1').replace('1', '0')
    b_bits = b.replace('0', '1').replace('1', '0')
    return a_bits.__xor__(b_bits)
    
    
