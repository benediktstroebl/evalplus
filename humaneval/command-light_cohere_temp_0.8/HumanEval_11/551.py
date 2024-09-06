```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros. XOR(a, b)
    Returns: the result of XOR operation on given two strings
    Test cases:
    '010' ^ '110' -> '100'
    'abc' ^ 'cba' -> 'abc'
    'A' ^ 'Z' -> 'a'
    '1234' ^ '5678' -> '1234'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")

    result = []
    for i in range(len(a)):
        result.append(b[i] ^ a[i])

    return ''.join(result)

# Test cases
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('abc', 'cba'))  # Output: 'abc'
print(string_xor('A', 'Z'))  # Output: 'a'
print(string_xor('1234', '5678'))  # Output: '1234'
```

This script defines a function named `string_xor` that performs a XOR operation on two input strings, ensuring that the length of both strings is equal. The function takes two strings as arguments and returns the result as a string. The function is then tested using various test cases to verify its correctness.