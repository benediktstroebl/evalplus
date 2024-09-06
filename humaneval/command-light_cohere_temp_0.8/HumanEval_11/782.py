```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    :return the string('0' * len(a) + len(b) - 1) - b + a
    """
    return ("0" * (len(a) + len(b) - 2)) - b + a
```
Test cases are provided within the script, passing different inputs (str2, "10", "01", etc.) The expected output is also printed out for each test.