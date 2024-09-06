from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert inputs to 8-bit strings (since XOR is 8-bit)
    a = ''.join(chr(int(c)) for c in a)
    b = ''.join(chr(int(c)) for c in b)

    # perform XOR on 8-bit strings
    xor = 0
    for i in range(len(a)):
        if a[i] == '1':
            xor ^= 1
        elif b[i] == '1':
            xor ^= 1
        else:
            xor ^= 0
    xor_str = ''.join(['1' if x else '0' for x in xor])
    return xor_str
