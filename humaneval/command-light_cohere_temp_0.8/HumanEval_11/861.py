```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings.
    Returns: from strings of only ones and return the result as a string.
    """
    XOR = '101'
    return X

# Test cases
test_string_xor = [
    ("010", "110"),
    ("00100", "1"),
    ("1111", "0"),
    ("abc", "b"),
    ("", "")
]

for case in test_string_xor:
    actual = string_xor(*case)
    assert actual == case[1], "Actual string does not match expected"
```