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
    ValueError: If either input string contains characters other than 1 and 0.
    """

    # Check if input strings are valid (only contain 1s and 0s)
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain 1s and 0s.")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Use zip to iterate over characters in both strings simultaneously
    # Use a list comprehension to perform XOR on corresponding characters
    # Convert the result back to a string
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```