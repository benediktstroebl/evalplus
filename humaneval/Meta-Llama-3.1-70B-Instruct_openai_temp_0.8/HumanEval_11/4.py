```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If the input strings are not the same length.
    ValueError: If the input strings contain characters other than '1' and '0'.
    """
    # Check if the input strings are the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be the same length")

    # Check if the input strings contain only '1' and '0'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of '1' and '0'")

    # Use zip to iterate over the characters of both strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # Convert the result to a string using join
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Test error handling
try:
    print(string_xor('010', '1110'))  # Raises ValueError
except ValueError as e:
    print(e)

try:
    print(string_xor('012', '110'))  # Raises ValueError
except ValueError as e:
    print(e)
```