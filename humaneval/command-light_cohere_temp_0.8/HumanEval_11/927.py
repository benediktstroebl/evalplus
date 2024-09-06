```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ 
    XOR two strings
    """
    return ''.join(a ^ b)

# Test cases
cases = [
    ("010", "110"),
    ("abc", "abc"),
    ("", ""),
    ("111", "0"),
    # Add more test cases here
]

for a, b in cases:
    print(f"XOR({a}, {b}): {string_xor(a, b)})
```