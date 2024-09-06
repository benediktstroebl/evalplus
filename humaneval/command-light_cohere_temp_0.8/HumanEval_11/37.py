```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
test_cases = [
    "010", "110", "1001",
    # Add more tests as needed
]

for case in test_cases:
    print(string_xor(case, case)))
```

This code defines a Python function named `string_xor` that performs a XOR operation on two input strings consisting of only digits (0s and 1s). The function returns a single string that represents the XOR of the input. The function is designed using Python's `type` annotation, which allows us to specify the types of the function's parameters and return value. 

The test cases are defined as a list of strings that the `string_xor` function is supposed to process. These test test process the accepted strings are "010", "110", and "1001". The test suite iterates over each test case and calls the `string_xor` function with the corresponding input strings.

The output will display the result of each test case, which will be the XOR of the input strings.