from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to list of characters
    a_chars = a.split()
    b_chars = b.split()
    # Sort characters in each string
    a_chars.sort()
    b_chars.sort()
    # Perform binary XOR operation
    xor_chars = []
    for i in range(len(a_chars)):
        if a_chars[i] == '0':
            xor_chars.append(b_chars[i])
        else:
            xor_chars.append('0')
    # Convert XOR characters back to string
    return ''.join(xor_chars)

