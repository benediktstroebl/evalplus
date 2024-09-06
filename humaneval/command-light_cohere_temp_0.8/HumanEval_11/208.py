```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings of only ones and zeros
    Returns: the result of applying bitwise XOR (^) to each character of strings a and b
    Test:  '010' XOR '110'
    """
    # Convert to list of characters
    a = ''.join(a)
    b = ''.join(b)
    # Use list comprehension to XOR
    result = [''] * len(a)
    for i, x in enumerate(a):
        result[i] = str(x ^ b[i])
    return ''.join(result)
# Test cases
print(string_xor('010', '110'))  # Expected output: 100
print(string_xor('abc', '1234'))  # Expected output: 5678
```
This Python script defines a function `string_xor` that performs the bitwise XOR operation on two input strings, which are expected to contain only the characters '0' and '1'. The function returns the result as a single string.  The also includes test cases to validate the function's correctness.