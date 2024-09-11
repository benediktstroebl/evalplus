```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'}):
        # Initialize an empty string to store the result
        result = ''
        # Iterate over the characters in the input strings
        for i, j in zip(a, b):
            # Perform XOR operation on the current bits
            result += str(int(i) ^ int(j))
        # If one string is longer than the other, append the remaining bits
        result += a[len(b):] if len(a) > len(b) else b[len(a):]
        # Return the result
        return result
    else:
        # Raise an error if the inputs are not valid binary strings
        raise ValueError("Inputs must be binary strings")

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function checks if the inputs are valid binary strings and raises a `ValueError` if they are not. It then iterates over the characters in the input strings, performs the XOR operation on each pair of bits, and appends the remaining bits if one string is longer than the other. The function is tested with two example inputs.