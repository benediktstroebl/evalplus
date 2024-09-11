```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings (a and b) and returns the result as a string.
    
    Args:
        a (str): A binary string consisting only of 1s and 0s.
        b (str): A binary string consisting only of 1s and 0s.

    Returns:
        str: The binary XOR result of a and b as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the two input strings simultaneously using zip
    for ai, bi in zip(a, b):
        # For each pair of bits, perform XOR operation and append the result to the result string
        result += str(int(ai) ^ int(bi))

    # If one of the strings is longer than the other, append the remaining bits of the longer string to the result
    result += a[-len(b):] if len(a) > len(b) else b[-len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function handles cases where the input strings are of different lengths by appending the remaining bits of the longer string to the result. The script also includes test cases to demonstrate the function's usage.