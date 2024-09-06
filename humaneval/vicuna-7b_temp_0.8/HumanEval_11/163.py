from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_bits = [int(c) for c in a]
    b_bits = [int(c) for c in b]
    xor_bits = []
    while len(a_bits) > 0 or len(b_bits) > 0:
        if a_bits[-1] == 1 and b_bits[-1] == 1:
            xor_bits.append(2 * a_bits.pop() + b_bits.pop())
        elif a_bits[-1] == 1 and b_bits[-1] == 0:
            xor_bits.append(a_bits.pop() + 2 * b_bits.pop())
        else:
            xor_bits.append(b_bits.pop() + a_bits.pop())
    return ''.join(str(xor_bits[i]) for i in range(len(xor_bits)))

