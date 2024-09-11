```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    if len(a)!= len(b):
        raise ValueError("Input strings must be the same length")

    # Perform binary XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Outputs: '100'
```