```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    Args:
        a (string),
        b (string)
    """
    return "".join(chr((ord(a[i]) ^ ord(b[i])) if a[i] == b[i] else 0) for i in range(len(a)))

# Test cases
def test_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("0011", "1010") == "1010"
    assert string_xor("000", "1111") == "1111"
    assert string_xor("abc", "cba") == "bba"
    assert string_xor("", "") == ""
    assert string_xor("ABC", "") == "C"
    assert string_xor("123", 10) == "123"

if __name__ == "__main__":
    test_xor()
```
The function returns the XOR of two input strings consisting only of ones and zeros, the function performs a binary XOR operation on every character of the input strings and returns the result as a string.