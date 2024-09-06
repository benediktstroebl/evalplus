```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only digits 1 and 0
    """
    return ''.join(c^d for c,d in zip(a, b))

# Test cases
tests = [
    ("010", "110"),
    ("1001", "1"),
    ("1010", "101"),
    ("1111", "001"),
    # Add more tests as needed
]

for a, b in tests:
    got = string_xor(a, b)
    assert got == "".join(c^d for c,d in zip(a, b))
``` 
This code defines a function `string_xor` that performs the XOR operation on two input strings, consisting only of the digit '1'. The function takes two strings as input and returns their XOR as a single string.