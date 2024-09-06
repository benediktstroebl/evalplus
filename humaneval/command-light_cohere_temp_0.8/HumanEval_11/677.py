```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0
    """
    assert len(a) == len(b), "Input strings must be the same length!"
    assert all(c == c for c in a), "Input strings must consist only of digits 1"
    assert all(c == c for c in b), "Input strings must consist only of digits 1"
    return str(bin(ord(ord(a[i]) ^ ord(b[i]))))[2:]

# Test suite
tests = [
    {
        "tests": [
            ("010", "110", "100"),
            ("1010", "1110", "100"),
            ("1001", "1011", "1010"),
            # Add more test cases as needed
        ],
        "expected": ["100"]
    },
]

# Run the tests and print the results
print("Test Results:", tests)
for test, expected in tests['tests']:
    act = string_xor("".join(test) + "0")
    print(f"Expected: {expected}, Actuals: {act}")
```