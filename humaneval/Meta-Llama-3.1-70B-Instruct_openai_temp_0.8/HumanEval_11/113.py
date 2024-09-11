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
        str: Binary XOR of a and b as a string.

    Raises:
        ValueError: If input strings contain characters other than 1 and 0.
    """

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Input strings must contain only 1s and 0s")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Use zip to pair corresponding bits from a and b
    # Use a list comprehension to XOR each pair of bits
    # Convert the result back to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test cases
print(string_xor('010', '110'))  # '100'
print(string_xor('1010', '1111'))  # '0101'
print(string_xor('0', '1'))  # '1'
print(string_xor('1', '0'))  # '1'
```