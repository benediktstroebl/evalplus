```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a (str): First string.
        b (str): Second string.

    Returns:
        str: XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ''

    # Iterate over the input strings
    for i in range(max(len(a), len(b))):
        # Get the current bits from both strings
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'

        # Perform XOR operation and append the result to the result string
        result += str(int(bit_a) ^ int(bit_b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script uses a simple iteration over the input strings to perform the binary XOR operation. It checks if the inputs are valid before performing the operation and raises a ValueError if they are not. The XOR result is then returned as a string. The example use cases are included at the end of the script for demonstration purposes.