from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError(
            f"length of input strings are not same, got {len(a)} and {len(b)}"
        )

    if a == '0' and b == '0':
        return a
    elif a == '1' and b == '1':
        return b
    else:
        a_len = bytes(str(a).encode())
        b_len = bytes(str(b).encode())
        b_xor = bytes(binascii.xor(a_len, b_len))
        return b_xor.hex()

