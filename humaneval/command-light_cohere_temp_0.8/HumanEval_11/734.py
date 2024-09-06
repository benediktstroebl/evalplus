```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function performs binary XOR operation on two input strings a and b consisting only of 1s and 0s.
    Return the result as a concatenated string of input
    """
    return ''.join(a.join(b[::-1]))

# Test cases
tests = [
    ("010", "110"),
    ("1010", "01"),
    ("000", "000"),
    ("1111", "1111"),
    # Add more test cases here
]

for a, b in tests:
    print(f"Testing {a} XOR {b}: {string_xor(a, b)})
``` 
This code demonstrates a self-contained Python function named `string_xor` that performs the binary XOR operation on two input strings. It uses the advantage over concatenating the strings in reverse order and returns the result.