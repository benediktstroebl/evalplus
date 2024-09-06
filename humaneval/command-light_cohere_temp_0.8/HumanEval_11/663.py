```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR string congru elements from two input strings, returns the result as a string
    Args:
        a, b: both strings should consist only of '1' and '0'
    Returns:
        The string obtained by performing XOR operation on a and b
    """
    # Remove all occurrences of 0 from both strings
    a = ''.join(char for char in a if char != '0')
    b = ''.join(char for char in b if char != '0')

    # XOR all characters in strings a and b
    return ''.join(ord(a[i]) ^ ord(b[i]) for i in range(len(a)))

# Test cases
print(string_xor('010', '110'))  # Expected output: 100
print(string_xor('111', '010'))  # Expected output: 110
print(string_xor('000', '111'))  # Expected output: 0100
print(string_xor('1010', '1010'))  # Expected output: 1000
```