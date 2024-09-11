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
        str: The binary XOR result of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    result = ''.join('1' if (a_i == '1' and b_i == '0') or (a_i == '0' and b_i == '1') else '0' for a_i, b_i in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('1010', '1010'))  # Expected output: '0000'
print(string_xor('1111', '0000'))  # Expected output: '1111'
```

This script defines a function `string_xor` that performs binary XOR on two input strings. It uses a generator expression within the `join` method to iterate over the characters of both strings in parallel, applying the XOR logic to each pair of bits. If the input strings have different lengths, it raises a `ValueError`. The script then includes example use cases to demonstrate the function's behavior.