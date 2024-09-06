```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only 1s and 0s
    """
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("000", "111"),
    ("1010", "01"),
    ("1111", "0"),
    ("111", "111")
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "01", f"Test case ({a}, {b}) failed: {result}"
```  This function performs the XOR operation on two input strings, both of which contain only characters '1' and '0'.  The test cases ensure that the function works correctly for various inputs, and the output is validated against the expected result.