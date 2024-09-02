from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_set = frozenset(a)
    b_set = frozenset(b)
    xor_string = set()
    for bit in itertools.product(a_set - b_set, repeat=2):
        xor_string.add(f'{bit[0]} X {bit[1]}' if bit[0] != 0 else f'{bit[1]} X {bit[0]}' if bit[1] != 0 else bit[1])
    return ' '.join(xor_string)

