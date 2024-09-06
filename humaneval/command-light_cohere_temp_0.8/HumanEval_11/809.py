```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s """
    return ''.join(c ^ d for c, d in zip(a, b))

# Test cases
tests = [
    ("010", "110", "100"),
    ("001", "11", "10"),
    ("000", "100", "101"),
    ("1010", "0110", "1111"),
    # Add more tests here as needed
]

for a, b in tests:
    print(string_xor(a, b))
```  This code defines a function `string_xor` that performs the XOR operation on two input strings, which consists only of the characters '1' and '0'. The function uses the `^ ^ operator` to perform the XOR operation and returns the result as a string.  The result of the output is then printed for each test case.