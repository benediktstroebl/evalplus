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
        str: Result of binary XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        # The XOR operation in binary is equivalent to addition modulo 2
        result += str((int(char_a) + int(char_b)) % 2)

    # If the input strings are of different lengths, append the remaining characters
    result += a[len(b):] if len(a) > len(b) else b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function uses the property of binary XOR that it is equivalent to addition modulo 2 to perform the operation. If the input strings are of different lengths, the remaining characters are appended to the result. The script also includes example use cases and a test to demonstrate the function's correctness.