```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the XOR operation as a binary string.

    Raises:
        ValueError: If the input strings contain non-binary characters.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if the input strings contain only binary characters
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must contain only binary characters.")

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Perform the XOR operation using the ^ operator and convert the result back to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: 100

# Test with invalid input:
try:
    print(string_xor('012', '110'))
except ValueError as e:
    print(e)  # Output: Input strings must contain only binary characters.

try:
    print(string_xor('01', '110'))
except ValueError as e:
    print(e)  # Output: Input strings must have the same length.
```