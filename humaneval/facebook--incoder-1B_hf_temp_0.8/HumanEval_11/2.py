from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_len = len(a)
    b_len = len(b)
    if a_len!= b_len:
        raise ValueError('Invalid input')

    a_chars = []  # type: List[str]
    b_chars = []  # type: List[str]

    for char in a:
        a_chars.append(str(int(char)))

    for char in b:
        b_chars.append(str(int(char)))

    xor_result = 0
    for a_char in a_chars:
        xor_result += a_char.xor(b_chars[len(a_chars)])

    return str(int(xor_result))

