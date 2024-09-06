```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, consisting only of ones.
    a = [c for c in a if c == '1']
    b = [d for d in b if d == '1']
    return ''.join([c^b for c in a for c in b])

# Test
test_cases = [
    "010", "110", "100",
    "001", "1010", "0110",
]
for t in test_cases:
    actual = string_xor(t, t)
    assert actual == t, f"Actual: {actual}, Expected: {t}"
```  This code defines a function **string_xor** that performs a XOR operation on two input strings, consisting only of ones. It uses a string representation of numbers and performs the XOR operation in-to-string. The code also provides a test cases and verifies that the output of the function matches the expected result.