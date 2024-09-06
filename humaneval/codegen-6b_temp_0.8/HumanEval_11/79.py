from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def str_to_int(x: str) -> int:
        res = 0
        for i in range(len(x)):
            res = res * 2 + int(x[i])
        return res

    # split result into groups of 8, max is 64 bits, so use 64 bits for
    # fast-modulo operation with the group size of 8
    a_len = len(a)
    b_len = len(b)
    mod = 2 ** 64
    if a_len <= b_len:
        a, b = b, a
    result = ""
    for i in range(a_len):
        result += format(str_to_int(a[i]) ^ str_to_int(b[i]), "016b")
    return result

