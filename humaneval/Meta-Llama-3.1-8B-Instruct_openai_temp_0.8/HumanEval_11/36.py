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
        str: Result of binary XOR operation.

    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Perform XOR operation on each character in the strings
    for char_a, char_b in zip(a, b):
        # If the characters are different, it's 1, else it's 0
        result += str(int(char_a) ^ int(char_b))
    
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes docstrings with examples and error checking to ensure the input strings are of the same length.