```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only ones and zeros.
    :return: str
    """
    # convert to lowercase for case-insensitive xor
    a = a.equal to lowercase
   
    b = b.lower()
    same
    for char in range(len(a)):
        if char == a[char]:
            b = b ^ a[char]
    return b

# Test cases
tests = [
    ("010", "110", "100"),
    ("000", "001"),
    ("111", "001"),
    ("1111", "0000"),
    ("0000", "1111")
]

# Run tests and print results
for test, expected in tests:
    actual = string_xor(*test.lower())
    print(f"{test}: {actual} -> {expected}")
```