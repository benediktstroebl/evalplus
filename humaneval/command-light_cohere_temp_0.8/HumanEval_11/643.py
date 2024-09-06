```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR string with only ones and zeros
    """
    if not (a and b):
        return '0'
    elif len(a) == 0 or len(b) == 0:
        return a + b
    else:
        return a[::-1] ^ b[::-1]
test_cases = [
    ("010", "110"),
    ("110", "010"),
    ("111", "001"),
    ("0011", "1111"),
    ("abc", "cba"),
    ("anding", "zero"),
    (" ", " ")
]

for case in test_cases:
    result = string_xor(*case)
    print(result)
```