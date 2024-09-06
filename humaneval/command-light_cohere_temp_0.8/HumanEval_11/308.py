```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) if a[i] != b[i] else a[i]
    for i in range(len(a)))

def test_string_xor():
    assert string_xor('010'.join', '110'.endswith('100')
    assert string_xor(''101010').startswith('10')
    assert string_xor(''101010', '').
    assert string_xor(''101010', '1010').startswith('10')
    assert string_xor(''101010', '01').endswith('1')

if __name__ == "__main__":
    test_string_xor()
```
Do you want me to help you with anything else?