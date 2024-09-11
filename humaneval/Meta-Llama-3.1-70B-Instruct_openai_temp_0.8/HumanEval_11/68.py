```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR operation on a and b.

    Raises:
        ValueError: If either a or b contains characters other than '0' or '1'.
    """

    # Check if both strings have the same length and only contain '0' or '1'
    if len(a)!= len(b) or not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must have the same length and only contain '0' or '1'.")

    # Use zip to iterate over both strings in parallel
    # Use a list comprehension to perform XOR operation on corresponding characters
    # Convert the result to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```