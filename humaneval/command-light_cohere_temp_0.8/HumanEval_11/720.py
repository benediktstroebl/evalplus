```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    return ''.join(a^ ^ b)

# Test cases
test_cases = [
    ("010", "110", "100"),
    ("001000", "1111"),
    ("abc", "abc"),
    ("abc", ""),
    ("", "")
]

# Test function
def test():
    for a, b in test_cases:
        result = string_xor(a, b)
        assert result == ''.join(a ^ b)

# Run the test
test()
```

I have provided a self-contained Python script that defines a function `string_xor` that performs a XOR operation between two strings, and tests the function with a series of test cases.  This also contains a test cases to check the correctness of the function.