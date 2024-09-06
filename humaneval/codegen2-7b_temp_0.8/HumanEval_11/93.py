from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(
        "{}{}".format(s[0], s[1]) if s[0] == s[1] else s[0]
        for s in zip(a, b)
    )

