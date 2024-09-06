from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    string_a = "".join(str(i) for i in a)
    string_b = "".join(str(i) for i in b)
    string_c = "".join(str(i * 2 + j) for i in range(len(string_a)) for j in range(len(string_b)))
    return "".join(str(not(i * 2 + j)) for i in range(len(string_c)) for j in range(len(string_c)))
