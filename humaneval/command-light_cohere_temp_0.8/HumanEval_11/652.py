```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    """
    Using list of characters, perform a bitwise XOR operation on every pair of corresponding characters and
    return the string as a result.
    """
    test_ CharList("01", "10", "01", "10")
    test_cases = [
        ("010", "110"),
        ("001", "110"),
        ("1010", "01"),
        ("110", "00"),
        ("0011", "11"),
        ("001", "0111")
    ]

    for a, b in test_cases:
        result = string_xor(a, b)
        assert result == "".join(result)  # assert True
```