```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b consisting only of 1s and 0s.
    The results a result, return as a string.
    """
    a: str, b: str)
    # Validate inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Input must be strings")
    # Initialize
    xor_string = ""
    for i in range(len(a)):
        if a[i] == '1':
            xor_string += '0'
        else:
            xor_string += '1'
    return xor_string

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("1010", "10"),
    ("11", "10"),
    # Additional tests can be added here
]

for act, expect in test_cases:
    actual = string_xor(act, act)
    if actual != expect:
        raise ValueError("Unexpected result")
```  This code defines a function `string_xor` that takes two strings as input and returns the XOR of these two strings. It then defines a test cases with a list of strings. The function is then called with each test case and the results are compared against the expected values to ensure the correctness of the function.