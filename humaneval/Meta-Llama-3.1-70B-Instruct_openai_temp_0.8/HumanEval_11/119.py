```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than 1 and 0.
    """
    # Check if input strings are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only contain 1s and 0s")

    # Perform binary XOR operation
    result = ''
    for i in range(max(len(a), len(b))):
        # Handle strings of different lengths by padding with zeros
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'
        result += str(int(bit_a) ^ int(bit_b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```