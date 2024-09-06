```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two input strings consisting only of ones and zeros and return the result as a string. """
    For algorithm:
        XOR(a[i], b[i]) for all i in the input strings.
    """
    generate the string consisting of ones and zeros
    return ''.join """
# Test case
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("000", "000"),
    ("111", "000"),
    ("0000", "111")
]

print("Results of XOR operation:")
[result for _, result in zip(test_cases, [string_xor(*c) for c in test_cases])]
```