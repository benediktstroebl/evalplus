from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    output = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            output += "0"
        elif a[i] == "0" and b[i] == "0":
            output += "1"
        elif a[i] == "1" and b[i] == "0":
            output += "1"
        else:
            output += "0"
    return output

