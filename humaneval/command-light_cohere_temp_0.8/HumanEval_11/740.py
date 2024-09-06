```python
import stringio
from typing import List


def string_xor(a: str, b: str) -> str:
    return stringio.sample(a) ^ b


# Test the function with some string inputs
test_cases = [
    ("010", "110"),
    ("0011", "1111"),
    ("1010", "1111"),
    # Add more test cases as needed
]
for a, b in test_cases:
    assert string_xor(a, b) == "100"
```