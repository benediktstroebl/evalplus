```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length.")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both input strings must consist only of 1s and 0s.")

    # Use the XOR operator (^) on each pair of corresponding bits
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Outputs: '100'
```