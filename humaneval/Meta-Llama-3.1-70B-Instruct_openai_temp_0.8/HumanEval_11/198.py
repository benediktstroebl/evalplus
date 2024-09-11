```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either string contains characters other than '1' or '0'.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '1' and '0'.")

    # Perform XOR on corresponding characters in the strings
    # The zip function stops at the end of the shorter string
    xor_result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    # If the strings are of different lengths, pad the shorter string with zeros
    # and continue the XOR operation
    if len(a) > len(b):
        xor_result += ''.join(str(int(x) ^ 0) for x in a[len(b):])
    elif len(b) > len(a):
        xor_result += ''.join(str(int(y) ^ 0) for y in b[len(a):])

    return xor_result


# Test the function
print(string_xor('010', '110'))  # Outputs: 100
print(string_xor('1010', '1100'))  # Outputs: 0110
```