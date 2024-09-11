```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function takes two binary strings as input, performs binary XOR operation
    and returns the result as a string.

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
        raise ValueError("Both strings must have the same length.")

    # Check if both strings contain only '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0's and '1's.")

    # Perform binary XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```