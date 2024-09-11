```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary XOR result of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length")

    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test cases
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('1010', '1100'))  # Expected output: '0110'
```
This Python script defines the `string_xor` function to calculate the binary XOR of two input strings. It then includes test cases to demonstrate the function's correctness.