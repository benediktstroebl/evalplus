```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid strings of 1s and 0s
    if set(a).issubset('10') and set(b).issubset('10'):
        # Perform XOR operation on corresponding bits
        return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    else:
        raise ValueError("Inputs must consist only of 1s and 0s")


# Run tests
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
try:
    print(string_xor('123', '456'))  # Expected error: ValueError
except ValueError as e:
    print(e)
```

In this script, the `string_xor` function performs binary XOR operation on two input strings by comparing corresponding bits. It checks if the inputs are valid strings of 1s and 0s before performing the operation. If the inputs are not valid, it raises a `ValueError`.