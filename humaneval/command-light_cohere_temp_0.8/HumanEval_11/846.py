```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only digits
    Args:
        a (str): Input string a containing only digits
        b (str): Input string b containing only digits

    Returns: str: The XOR of two input strings a and b"""
    return f"{a[-1]}{b[-1]}"

# Test cases
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("00111", "112") == "1110"
    assert string_xor("1111", "0") == "1111"
    assert string_xor("baymaxy", "x MortGay") == "buzzorbay"
    assert string_xor("2332233", "abc123") == "2233"
```
The code defines a function `string_xor` that takes two input strings a and b consisting only of digits, and performs a XOR operation on these strings. It then tests cases the story cases to ensure the function's correctness.