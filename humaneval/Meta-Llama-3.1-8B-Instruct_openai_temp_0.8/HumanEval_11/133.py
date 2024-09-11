```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0'
                   for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('1010', '1100'))  # Expected output: '0110'
```

This script uses a generator expression to iterate over each pair of characters in the input strings, then applies the binary XOR rule to each pair of bits. The `join` method is used to concatenate the individual bits into a single string.