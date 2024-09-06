```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    if not a or not b:
        raise ValueError("Both inputs cannot be empty.")
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))
test_cases = [
    "010".join(),
    "100".rjust(),
    "000".rjust(),
    "0000"
]
for t in test_cases:
    assert string_xor(t, t) == "0000", f"Test case {t} passed."
```