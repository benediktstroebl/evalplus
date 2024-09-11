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
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the input strings and perform XOR operation
    for char_a, char_b in zip(a, b):
        # Use the XOR operator (^) to perform binary XOR
        result += str(int(char_a) ^ int(char_b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation to ensure that the input strings have the same length and handles the XOR operation using the `^` operator in a loop to build the result string. The script also includes a test case to demonstrate the function's behavior.