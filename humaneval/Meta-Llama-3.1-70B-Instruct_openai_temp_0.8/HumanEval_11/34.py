```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.
    """
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip to iterate over the characters of the input strings in parallel
    # and the XOR operator (^) to perform the binary XOR operation
    # Convert the result back to a string using join
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```