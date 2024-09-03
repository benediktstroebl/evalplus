from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bytes = binascii.hexlify(a).decode("ascii")
    b_bytes = binascii.hexlify(b).decode("ascii")

    a_len = len(a_bytes)
    b_len = len(b_bytes)

    a_ints = [int(a_bytes[i: i + 2]) for i in range(0, a_len)]
    b_ints = [int(b_bytes[i: i + 2]) for i in range(0, b_len)]

    return "".join([chr(x ^ y) for x, y in zip(a_ints, b_ints)])

