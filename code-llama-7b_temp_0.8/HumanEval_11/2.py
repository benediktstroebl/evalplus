from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    assert all(
        char in ('0', '1') for char in a + b
    ), "Please input only 0s and 1s"
    return "".join("1" if a_bit == b_bit else "0" for a_bit, b_bit in zip(a, b))

