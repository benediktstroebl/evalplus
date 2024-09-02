from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert input strings to list of binary digits
    a_digits = [bin(c)[2] for c in a]
    b_digits = [bin(c)[2] for c in b]

    # perform binary XOR on the digits
    xor_digits = [a_digits[i] ^ b_digits[i] for i in range(len(a_digits)) if a_digits[i] != '0']

    # convert digits back to string
    xor_string = ''.join(chr(xor_digits[i]) for i in range(len(xor_digits)))

    return xor_string

