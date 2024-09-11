```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either of the input strings contains characters other than '0' and '1'.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings only contain '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must only contain '0' and '1'")

    # Use the built-in zip function to iterate over the characters of both strings in parallel
    # Use a generator expression to perform the XOR operation on each pair of characters
    # Convert the result to a string using the join function
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```