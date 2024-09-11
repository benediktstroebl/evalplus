```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Initialize an empty result string
    result = ""

    # Iterate over characters in input strings
    for i in range(len(a)):
        # Perform binary XOR operation on corresponding characters
        result += str(int(a[i]) ^ int(b[i]))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation to ensure both strings are of equal length and raises a `ValueError` if this condition is not met. The script also includes a test case to demonstrate the function's usage.