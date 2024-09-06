```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    We use the fact two strings and do XOR operation on a and b, and return the result as a string.
    """
    tests = [("01", "110"), ("01", "0"), ("10", "01")].
    for test_case in tests:
        got = string_xor(test_case[0], test_case[1])
        assert got == test_case[2], f"assertion failed for {test_case}"
    return "XOR Ok"
```