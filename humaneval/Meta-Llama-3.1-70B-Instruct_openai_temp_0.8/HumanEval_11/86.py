```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either of the input strings contains characters other than 1s and 0s.
    """

    # Check if the input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty list to store the result
    result = []

    # Perform XOR operation on each character of the input strings
    for char_a, char_b in zip(a, b):
        # XOR operation can be performed using the!= operator in Python
        result.append('1' if char_a!= char_b else '0')

    # Join the result list into a string and return
    return ''.join(result)


# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```