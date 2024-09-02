from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a = a.replace("1", "").replace("0", "").replace(" ", "")
    b = b.replace("1", "").replace("0", "").replace(" ", "")

    result = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result

