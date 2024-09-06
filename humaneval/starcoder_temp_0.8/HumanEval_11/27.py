from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert strings to binary
    a = a.replace('1', '11').replace('0', '00')
    b = b.replace('1', '11').replace('0', '00')
    # calculate binary xor
    c = [int(x) for x in a]
    d = [int(x) for x in b]
    for i in range(max(len(c), len(d))):
        if i >= len(c):
            c.append(0)
        if i >= len(d):
            d.append(0)
        c[i] = c[i] ^ d[i]
    # convert binary to string
    c = ''.join([str(x) for x in c])
    c = c.replace('11', '1').replace('00', '0')
    return c
