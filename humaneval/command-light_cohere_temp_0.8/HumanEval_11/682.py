```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings with only ones and zeros
    """
    return "".join(c ^ d for c, d in zip([0, a] + [0]))
test_cases = [
    ("010", "110"),
    ("001", "001"),
    ("111", "001"),
    ("1111", "110"),
    # Add more test cases here
]
for a, b in test_cases:
    print(f"XOR: {a} {b} = {string_xor(a, b)}")
```