```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two input strings a and b. string, return the result as a string.
    # Splits only by using ' ' and 0' only.
    return ''.join(a.join(b))

# Unit test
tests = [
    ("010", "110"),
    ("00", "10"),
    ("000", "001"),
    ("1010", "11"),
    ("110", "010"),
    ("1111", "1")
]
for a, b in tests:
    print(f"{a} XOR {b} = {string_xor(a, b)}")
```