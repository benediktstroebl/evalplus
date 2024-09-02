from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert all(x in "01" for x in a)
    assert all(x in "01" for x in b)

    result = ""
    for ai, bi in zip(a, b):
        if ai == bi:
            result += "0"
        else:
            result += "1"
    return result

