```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If the input strings are not of the same length or contain characters other than '0' and '1'.
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain only '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of '0' and '1'")

    # Perform binary XOR on the input strings
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function includes input validation to ensure that the input strings are of the same length and contain only '0' and '1'. The example usage at the end demonstrates how to use the function.