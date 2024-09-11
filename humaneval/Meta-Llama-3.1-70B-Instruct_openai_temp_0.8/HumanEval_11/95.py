```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either string contains characters other than '0' and '1'.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0' and '1'.")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")

    # Perform binary XOR using zip and a list comprehension
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Test with invalid input
try:
    print(string_xor('012', '110'))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Both strings must consist only of '0' and '1'.

# Test with inputs of different lengths
try:
    print(string_xor('010', '1100'))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Both strings must be of the same length.
```