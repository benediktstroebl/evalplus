```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR on two strings consisting only of ones and zeros.
    :param a strings a and b
    :return string containing result of XOR operation
    """
    return "".join(str(ord(c)) for c in map('00'[i % 2] for i in a + b))

#Test cases
test_cases = [
    ("010", "110", "100"),
    ("1010", "0110"),
    ("0011", "1110"),
    ("1001", "1011"),
    ("0000", "1111")
]

for a, b in test_cases:
    expected = "".join(str(ord(c)) for c in map('00'[i % 2] for i in a + b))
    print(f"Expected: {expected}\nActual: {string_xor(a, b)}")
```
This Python script defines a function `string_xor` that performs the XOR operation on two input strings. It uses the example test cases to demonstrate the functionality. The output should match the expected results.