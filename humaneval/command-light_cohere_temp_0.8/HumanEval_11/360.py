```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of digits 1 or 0
    Returns: result of performing XOR operation on input strings a and b.
    """ e.g.: '100110'
    strings a and b"""
    return a ^ b

def test():
    s = "010"
    b = "110"
    result = string_xor(s, b)
    assert result == "100"
    assert len(result) == 3
    assert set(result) == {"0", "1", "2"}

if __name__ == "__main__":
    test()
```