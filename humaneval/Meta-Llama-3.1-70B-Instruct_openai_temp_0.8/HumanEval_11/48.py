```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two binary strings.

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

    # Perform XOR operation using zip and a list comprehension
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```