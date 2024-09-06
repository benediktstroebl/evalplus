```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    """
    operation:
    101010
    1101110
    00000101
    1010101
    10101011
    """
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("111", "011") == "110"
    assert string_xor("000", "111") == "010"
    assert string_xor("1010", "1011") == "0110"
    assert string_xor("1010", "10110") == "000110"
if __name__ == "__main__":
    test_string_xor()
```