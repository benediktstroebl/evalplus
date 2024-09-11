```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): First string consisting of 1s and 0s.
        b (str): Second string consisting of 1s and 0s.

    Returns:
        str: Binary XOR result as a string.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty result string
    result = ''

    # Check if lengths of the input strings are equal
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Iterate over the input characters
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        # and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result

# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
```

This Python script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result as a string. It iterates over the input characters, performs a binary XOR operation on each pair of characters, and appends the result to a result string. The function raises a `ValueError` if the input strings are not of equal length. The script includes a test case to demonstrate the function's usage.