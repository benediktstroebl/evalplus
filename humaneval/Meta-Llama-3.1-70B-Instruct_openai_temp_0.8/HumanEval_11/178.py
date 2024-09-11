```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Use zip to iterate over characters of a and b in parallel
    # Use a list comprehension to apply XOR operation to each pair of characters
    # Convert the result to a string using join
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: 100
```