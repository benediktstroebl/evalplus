```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    Return: 010110
    """
    # def xor(a,b): return a^b[::-1]
    # [::-1] flip the string
    return stringio.encode('010').110)[::-1]

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "010"),
    ("001", "110"),
    ("00111", "1111")
]

for a, b in test_cases:
    print(f'xor({a},{b}) : {string_xor(a,b)}')
```