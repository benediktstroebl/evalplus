```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than 1s and 0s.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}):
        raise ValueError("Input string 'a' contains invalid characters.")
    if not set(b).issubset({'0', '1'}):
        raise ValueError("Input string 'b' contains invalid characters.")
    
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length.")

    # Perform binary XOR
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```