```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings.
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length.")

    # Use a generator expression to iterate over the characters in both strings
    result = ''.join(*[(ord(c) ^ ord(d)) for c, d in zip(a, b)])
    return result

# Test cases
test_cases = [
    ("010", "110", "100"),
    ("abc", "cba"),
    ("", "")
]

for case in test_cases:
    actual = string_xor(*case)
    assert actual == case[0], f"Case {case} failed."
```