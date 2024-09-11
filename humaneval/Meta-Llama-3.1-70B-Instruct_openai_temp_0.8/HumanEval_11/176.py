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
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either string contains characters other than '1' or '0'.
    """
    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '1' and '0'.")

    # Check if strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")

    # Perform binary XOR using zip and a list comprehension
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```