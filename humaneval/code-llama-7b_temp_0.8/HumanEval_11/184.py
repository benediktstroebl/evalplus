from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert len(a) == len(b), "Inputs must have same length"
    assert (
        set(a).issubset("10") and set(b).issubset("10")
    ), "Inputs must only have 1s and 0s"

    result = []
    for ai, bi in zip(a, b):
        if ai == bi:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)

