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
        str: The binary XOR result of a and b.

    Raises:
        ValueError: If either a or b contains characters other than '0' or '1'.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings contain only '0' or '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must contain only '0' or '1'")

    # Perform binary XOR on the two strings
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
```