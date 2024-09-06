Here's the solution:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return f'{a[i] ^ b[i] for i in range(len(a))}'.center()

# Sample Test cases
test_cases = [
    ("010", "110"),
    ("0011", "1110"),
    ("1010", "0110"),
    ("1111", "1010"),
    ("1000", "0000"),
]

for case in test_cases:
    print(f'Expected: "{case[0]} XOR {case[1]}")
    print(f' Got: "{string_xor(case[0], case[1])}")
```
This code defines a function `string_xor` that takes two strings as input and returns their XOR (which is also a string). It uses a list comprehension to apply the XOR operation to every character in the input strings, and then centers the result.