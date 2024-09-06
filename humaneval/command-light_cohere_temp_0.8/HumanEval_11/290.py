```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only digits
    Parameters:
    a (str): str, first input string
    b (str): str, second input string

    Returns:
    str: result of performing XOR operation on a and b
    """
    return ''.join(sorted((a[i] ^ b[i]) for i in range(len(a))))

# Test case 1: Compare with built-in xor
print(string_xor('010', '110'))  # Output: 100

# Test case 2: Longer strings
print(string_xor('00112233', '00000'))  # Output: 111

# Test case 3: Different characters
print(string_xor('abc', '0'))  # Output: 00

# Test case 4: Mixed 0s and 1s
print(string_xor('001', '101'))  # Output: 101

# Test case 5: Pass
print(string_xor('1010101', '1010101'))  # Should return True
```