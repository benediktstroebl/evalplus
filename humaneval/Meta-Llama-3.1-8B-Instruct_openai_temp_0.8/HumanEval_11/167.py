```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result of a and b.
    >>> string_xor('010', '110')
    '100'
    """
    if set(a).issubset('01') and set(b).issubset('01'):
        # Convert binary strings to integers, perform XOR, and convert back to binary
        return bin(int(a, 2) ^ int(b, 2))[2:]
    else:
        raise ValueError("Input strings must consist only of 1s and 0s.")

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function which takes two binary strings as input, performs a binary XOR operation, and returns the result as a string. It uses Python's built-in `bin` function to convert integers to binary strings, and the `^` operator to perform the XOR operation. If the input strings are not binary, it raises a ValueError.