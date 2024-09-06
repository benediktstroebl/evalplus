from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of only 1s and 0s.

    Parameters:
    - a (str): The first string for binary XOR.
    - b (str): The second string for binary XOR.

    Returns:
    - str: The result of binary XOR as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """

    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))