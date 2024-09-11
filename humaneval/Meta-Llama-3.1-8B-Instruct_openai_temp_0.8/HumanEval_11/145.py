```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.
    """
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize an empty string to store the XOR result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the corresponding characters
        # If char_a is '1' and char_b is '0', the result is '1', otherwise '0'
        result += "1" if (char_a == '1' and char_b == '0') or (char_a == '0' and char_b == '1') else "0"

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes a docstring that describes the function's behavior, arguments, and return value. Additionally, the script includes a check to ensure that the input strings have the same length and raises a `ValueError` if they do not.