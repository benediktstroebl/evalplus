```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings only contain 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must only contain 1s and 0s")

    # Perform XOR operation on each pair of characters
    result = ''.join('1' if c1!= c2 else '0' for c1, c2 in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '101'))  # Output: '000'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input, checks if they have the same length and only contain 1s and 0s, and then performs a binary XOR operation on each pair of characters. The result is returned as a string. The example use cases are provided at the end of the script to test the function.