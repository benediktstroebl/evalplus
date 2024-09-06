```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, returns the result as a string.
    Args:
    a: str, first input string.
    b: str, second input string.
    Returns: the XOR between the strings
    """
    return a^b

# Test cases
test_string_xor = [
    ("010", "110"),
    ("abc", "abc"),
    ("222", "11"),
    ("00", "10"),
    ("111", "101")
]

for case in test_string_xor:
    actual_result = string_xor(*case)
    assert actual_result == case[0] + case[1]
```