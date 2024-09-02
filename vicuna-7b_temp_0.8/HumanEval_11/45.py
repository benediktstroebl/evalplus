from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Use list to store the XOR of corresponding positions in a and b
    xor = [[0, 0] for _ in range(max(len(a), len(b)))]
    for i in range(max(len(a), len(b))):
        for j in range(i+1, len(a)):
            # If a and b have different digits at positions i and j,
            # add the XOR of these positions to the XOR list
            if a[i] != b[j]:
                xor[i][j] = a[i] ^ b[j]
            else:
                # If a and b have the same digit at positions i and j,
                # add the XOR of the next digit in a and b to the XOR list
                xor[i+1][j] = a[i+1] ^ b[j]
    return ''.join(['1' if xor[i][j] == 1 else '0' for i in range(len(xor)) for j in range(len(xor[i]))])

