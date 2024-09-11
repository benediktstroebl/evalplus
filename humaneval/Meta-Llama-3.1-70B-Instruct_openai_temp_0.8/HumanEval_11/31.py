```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result as a string.

    Raises:
    ValueError: If either input string contains characters other than '0' and '1'.

    Example:
    >>> string_xor('010', '110')
    '100'
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length")

    # Check if both strings only contain '0' and '1'
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both input strings must only contain '0' and '1'")

    # Use zip to iterate over both strings simultaneously
    # Use a list comprehension to perform XOR on corresponding bits
    # Convert the result back to a string
    return ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```