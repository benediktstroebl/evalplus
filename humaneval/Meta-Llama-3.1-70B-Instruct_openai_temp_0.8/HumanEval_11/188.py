```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either string contains characters other than '0' or '1'.
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings contain only '0' and '1'
    for char in a + b:
        if char not in ['0', '1']:
            raise ValueError("Both strings must consist only of '0' and '1'")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. The function checks if both strings have the same length and contain only '0' and '1' characters. It then iterates over the characters in the input strings, performs the XOR operation on each pair of characters, and appends the result to the result string. The script also includes a test case to demonstrate the function's usage.