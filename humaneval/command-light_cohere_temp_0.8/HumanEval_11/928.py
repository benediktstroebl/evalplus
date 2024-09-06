```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    """
    # validate input
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")

    # validate length
    if len(a) != len(b):
        raise ValueError("Both inputs must have the same length")

    # implement xor
    return ''.join(c ^ d for c, d in zip(a, b))

# test cases
test_cases = [
    ("010", "110"),
    ("abc", "abc"),
    ("" , ""),
    (b" ", a""),
    ("abc", "yzab"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "100"
```
The code defines a function `string_xor` that takes two strings as input and performs the XOR operation on them, returning the result as a single string. The function first validates the the inputs and checks whether the strings have the same length. If the inputs are invalid, a `TypeError` or `ValueError` is raised. The function uses the `zip` to iterate over the characters of the two strings and performs the XOR operation on each pair of characters. The test cases section contains several examples to validate the correctness of the `string_xor` function.