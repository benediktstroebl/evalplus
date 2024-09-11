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
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s")

    # Use zip to pair corresponding characters from both strings
    # Use a list comprehension to perform the XOR operation on each pair
    # Convert the result back to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```