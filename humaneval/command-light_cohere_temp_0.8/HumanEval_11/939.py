```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only 1s and 0s.
    Return the format:
    a = '0101010101010101'
    b = '110101010101'
    c = a ^ b
    return c

#Test cases
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("000", "111"),
    ("1010", "1010"),
    ("1000", "00"),
]

for act, expected in test_cases:
    got = string_xor(act, act)
    assert got == expected, f"Expected: {expected}, Act: {act}, Got: {got}"
```  This Python code defines a function named `string_xor` that performs the XOR operation on two input strings containing only the digit 1. The function takes two strings as arguments and returns the XOR of these strings. The code uses the string values and performs the XOR operation on these values, then compares the result against the expected output from the corresponding test case. The code also defines a list of test cases, where each element is a pair of two strings, and the expected output of the `string_xor` function for this pair of strings. The code then loops over the test cases and passes each test by comparing the actual output of the `string_xor` function with the expected output.