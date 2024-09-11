```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either input string contains characters other than 1 or 0.
    """

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must contain only 1s and 0s")

    # Check if input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Use zip to iterate over both strings simultaneously
    # Use a list comprehension to perform the XOR operation
    # Convert the result to a string using join
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```