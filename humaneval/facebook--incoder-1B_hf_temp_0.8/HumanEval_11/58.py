from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert string into list of binary numbers
    bin_a = [int(x, 2) for x in a.split('0')]
    bin_b = [int(x, 2) for x in b.split('0')]

    # Perform XOR on binary numbers
    result = ''
    for num in xrange(len(bin_a)):
        result += str(int(bin_a[x] ^ bin_b[x], 2))
    return result

