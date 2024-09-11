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

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Perform XOR operation on corresponding bits
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    # If the inputs have different lengths, pad the shorter one with zeros
    max_len = max(len(a), len(b))
    result = result.ljust(max_len, '0')

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '0101'))  # Output: '1111'
print(string_xor('1', '0'))  # Output: '1'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation and handling for inputs of different lengths. The example use cases demonstrate the function's usage.