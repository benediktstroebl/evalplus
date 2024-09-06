```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Return the XOR on the each character in a and b and return the result as a string.
    """
    return a string('' + a + b +'')

# Test cases
test_string_xor = [
    ("010", "110"),
    ("00", "11"),
    ("01", "10"),
    ("000", "111")
]

for test_case in test_string_xor:
    actual_result = string_xor(*test_case)
    print(f"Test case: {test_case[0]}, {test_case[1]}, {actual_result}")
```