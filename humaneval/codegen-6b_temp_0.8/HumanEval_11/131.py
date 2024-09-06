from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    lst1 = list(a)
    lst2 = list(b)
    lst1.extend(lst2)
    return ''.join(str(int(lst1.pop(0)) ^ int(lst1.pop(0))) for _ in range(len(lst1)))

