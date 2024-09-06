```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two given strings consisting only of ones and zeros. XOR is using bits of two integers.
    Return the string resulting from binary representation of these two numbers.
    """
    string_xor('010', '110')
    """
    return a ^ b

# Test cases for the above function
tests = [
    ("010", "110"),
    ("111", "110"),
    ("000", "111"),
    ("1111", "1111"),
    ("00", "11")
]

for i, test in enumerate(tests):
    result = string_xor(test[0], test[1])
    if result != tests[i][1]:
        print(f"Error in test {i+1} - Expected {tests[i][1]}, but got {result}")
        raise SystemExit
```