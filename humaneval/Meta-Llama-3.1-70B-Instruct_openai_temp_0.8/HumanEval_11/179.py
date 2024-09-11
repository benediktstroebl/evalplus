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
    ValueError: If either input string contains characters other than 1 or 0.

    Example:
    >>> string_xor('010', '110')
    '100'
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")

    # Check if both strings only contain 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must only contain 1s and 0s.")

    # Use the zip function to iterate over two strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # The XOR operation is performed by converting the characters to integers, performing the XOR operation, and converting back to strings
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```