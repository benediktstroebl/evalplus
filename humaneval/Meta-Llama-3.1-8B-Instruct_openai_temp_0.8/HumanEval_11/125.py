### Binary String XOR Function
#### Python Script
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of XOR operation as a binary string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length.")

    # Convert binary strings to integers, perform XOR, and convert back to binary
    result = bin(int(a, 2) ^ int(b, 2))[2:]

    # Make sure result is the same length as inputs
    result = result.zfill(max(len(a), len(b)))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1111', '0000'))  # Output: '1111'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a `string_xor` function that takes two binary strings as input, performs the XOR operation, and returns the result as a binary string. It includes input validation and example usage.