from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n1 = len(a)
    n2 = len(b)
    alist = [0] * n1
    blist = [0] * n2
    for i in range(n1):
        if a[i] == '1':
            alist[i] = 1
            blist[i % n2] = 1
    for i in range(n2):
        if b[i] == '1':
            alist[i % n1] = 1
            blist[i] = 1
    result = ''
    for i in range(n1):
        for j in range(n2):
            if alist[i] != blist[j]:
                result += '1'
        else:
            result += '0'
    return result

