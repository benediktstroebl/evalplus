```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of valid type and length
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length")

    # Use built-in zip function and XOR operator to get binary XOR result
    # list comprehension is used to convert list of boolean values to binary string
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a binary string. It includes input validation and handles potential errors that might occur due to invalid input.