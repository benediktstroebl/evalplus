```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings.
    Args:
        - string a
        - string b
    Returns: string resulting from XOR of a and b
    """
    return f"{a[-1]}{b[-1]}"

# Test suite
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("aa", "aa") == "aa"
    assert string_xor("", "") == ""
    assert string_xor("", "x") == "x"
    assert string_xor("123", "456") > "123"
```