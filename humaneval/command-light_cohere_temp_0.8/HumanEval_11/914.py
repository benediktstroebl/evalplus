```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings, ensuring only characters are '0' or '1'.
    : return xor(a, b)
    :return: str
    """
    # Convert to list of characters to perform XOR operation
    al = [c for c in a if c != '']
    bl = [c for c in b if c != '']

    # XOR the lists of characters
    return ''.join(al ^ bl)

# Test cases
test_cases = [
    ("010", "110")
    ("1010", "01"),
    ("0000", "1111")
    ("111", "100"),
    ("110", "11")
]

# Perform all tests in parallel
for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "100"
```
This code implements a string XOR operation, ensuring that only characters set to '1' are retained from the original strings. The code also has test cases to validate the correctness of the function. 

This is a self-contained solution to the problem of performing XOR operation on strings.