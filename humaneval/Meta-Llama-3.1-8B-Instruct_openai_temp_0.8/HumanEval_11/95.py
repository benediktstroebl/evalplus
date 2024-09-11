```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): First input string.
    b (str): Second input string.

    Returns:
    str: Result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'

    """
    # Check if inputs are strings consisting of 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation
        if char_a == char_b:
            result += '0'
        else:
            result += '1'

    # If the input strings have different lengths, append the remaining characters
    result += a[len(b):] if len(a) > len(b) else b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('1', '0'))      # Output: '1'
```

This script defines a function `string_xor` that takes two input strings `a` and `b` consisting of 1s and 0s, performs a binary XOR operation, and returns the result as a string. It includes error checking to ensure the inputs are valid strings consisting only of 1s and 0s. The function also handles cases where the input strings have different lengths by appending the remaining characters.