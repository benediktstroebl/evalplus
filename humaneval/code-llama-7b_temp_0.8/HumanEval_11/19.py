from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # all strings in Python3 are Unicode
    # Unicode characters have code points (integers)
    # code points can be converted to and from strings of hex digits
    # hex digits are integers in range(16)
    # casting code points to integers and back will not change the character
    # so we can perform all string operations on code points
    # then convert back to string
    codepoints = [ord(c) for c in a]
    for i, c in enumerate(b):
        codepoints[i] ^= ord(c)
    return "".join(chr(c) for c in codepoints)

