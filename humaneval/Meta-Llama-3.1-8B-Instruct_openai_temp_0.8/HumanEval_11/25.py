```python
from typing import List
import itertools

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR operation on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation on a and b.
    """
    # Check if inputs are binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be strings of 1s and 0s")

    # Perform XOR operation on two binary strings
    # This will give a list of 0s and 1s
    result = ''.join('1' if (x, y) in [(0, 1), (1, 0)] else '0' for x, y in zip(a, b))

    return result


# Test cases
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '110'))  # Expected output: '011'
```
This script includes input validation to ensure the function only processes binary strings. It then uses a list comprehension with `zip` to iterate over the two input strings and perform the binary XOR operation. The result is returned as a string.