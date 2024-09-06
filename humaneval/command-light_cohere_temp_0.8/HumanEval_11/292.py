```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    Returns the string xor(a, b)"""
    return str(list(map(lambda x: int(x) - int('0') if x == '0' else int(x), a + b)))

# Test cases
test_cases = [
    ("010", "110", "100"),
    ("000", "111"),
    ("1010", "01"),
    ("1010", "10"),
    ("1101", "001"),
    ("0011", "11"),
    ("1111", "1")
]

for i, (a, b) in enumerate(test_cases):
    result = string_xor(a, b)
    print(f"Test {i+1}: {a} XOR {b} = {result}")
``` 
This code provides a function `string_xor` that performs the XOR operation on two input strings, consisting only of digits 1 and 0. The test cases are defined to validate the functionality, and the output is printed for each test case.