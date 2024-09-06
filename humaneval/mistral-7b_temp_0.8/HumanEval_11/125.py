from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    a_len, b_len = len(a), len(b)
    for i in range(max(a_len, b_len)):
        if i >= a_len:
            result += "0"
        elif i >= b_len:
            result += "1"
        elif a[i] == "1" and b[i] == "1":
            result += "0"
        elif a[i] == "0" and b[i] == "0":
            result += "1"
        elif a[i] == "0" and b[i] == "1":
            result += "1"
        else:
            result += "0"
    return result

