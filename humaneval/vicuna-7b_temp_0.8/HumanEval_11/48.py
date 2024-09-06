from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert to binary
    a_bin = ''.join(['1' if c == '0' else '0' for c in a])
    b_bin = ''.join(['1' if c == '0' else '0' for c in b])

    # XOR binary numbers
    a_xor = 0
    b_xor = 0
    for i in range(len(a_bin)):
        a_xor += a_bin[i] * 2 ** (len(a_bin) - i - 1)
        b_xor += b_bin[i] * 2 ** (len(b_bin) - i - 1)

    # Convert back to string
    result = ''.join(['1' if (a_xor & b_xor) == 0 else '0' for a_xor in a_xor])

    return result

