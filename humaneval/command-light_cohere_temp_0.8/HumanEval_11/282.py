```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    :param
        string a a and b: Converted to lists of characters and perform XOR.
    :return: Converted back string
    """
    a = sorted(a)
    b = sorted(b)
    return ''.join(''.join(sorted((c1 ^ c2) for c1, c2 in zip(a, b)))

# Test cases
test_cases = [
    ("010", "110"),
    ("abc", "cba"),
    ("wxyz", "uvwxyz"),
    ("1234567890", "891234567890"),
    # Add more test cases as needed
]

for act, expect in test_cases:
    print(f"{act} XOR {expect} = {string_xor(act, expect)}")
```
The function string_xor takes two strings a and b as input and returns the XOR of the two strings.