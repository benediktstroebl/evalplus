```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Function performs a bitwise XOR operation on two input strings.
    Returns the
            result of the input strings, 'a' and 'b'.
    """
    # XOR each character of strings
    return ''.join(c^b for c in a)

# Test cases
test_cases = [
    ("010", "110"),
    ("00", "10"),
    ("001", "011"),
    ("1010", "0110"),
    ("1000", "0000")
]

for case in test_cases:
    actual = string_xor(*case)
    assert actual == case[0] + case[1], "AssertionError: Test failed"
```  This function performs a bitwise XOR operation on two input strings, consisting only of ones and zeros, and returns the result as a string.