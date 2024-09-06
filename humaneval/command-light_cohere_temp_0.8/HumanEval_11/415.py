```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function to perform XOR on two input strings a and b.
    :type a Input strings a and return their XOR
    """
    # Ensure both inputs are strings
    assert isinstance(a, str) and isinstance(b, str), "Both inputs must be strings"
    # XOR of two strings
    return f"{a[0]}{b[0]}".join(f"{a[1]}{b[1]}".join(str))

# Test cases
test_cases = [
    ("010", "110"),
    ("100", "01"),
    ("111", "11"),
    ("001", "01"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "".join(result), f"Result: {result}, Expected: '{'.join(b)'}"
```