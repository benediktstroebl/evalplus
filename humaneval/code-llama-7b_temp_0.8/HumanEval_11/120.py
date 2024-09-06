from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_array = [c for c in a]
    b_array = [c for c in b]
    result = [
        "1" if (c1 == c2) else "0"
        for c1, c2 in zip(a_array, b_array)
    ]
    return "".join(result)

