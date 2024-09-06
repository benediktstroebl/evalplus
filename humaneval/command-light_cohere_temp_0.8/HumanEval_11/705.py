```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters, numbers, and space.x.
    Perform binary XOR by on the inputs and return result as a string.
    """
    example:
    >>> string_xor('010', '110')
    '100'
    """
    # or XOR operator
    return ''.join(c if c in a else c in b)

# Test case 1
test_cases = [
    ("001", "1010"),
    ("abc", "bcca"),
    ("foo", "foo"),
    ("bar", "bar"),
    ("1000", "1"),
    ("abc", "123")
]

for a, b in test_cases:
    expected = "".join(c if c in a else c in b)
    print(f"Test case {a} and {b} - Expected: {expected}, Actual: {string_xor(a, b)}")
```