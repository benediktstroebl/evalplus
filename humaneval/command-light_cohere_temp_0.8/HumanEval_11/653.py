```python
import stringcase
import pytest

def string_xor(a: str, b: str) -> str:
    """ XOR two strings, a and b, consisting only of ones and zeros
    """
    assert len(a) == len(b)
    assert all(c == '0' for c in a) and all(c == '0' for c in b)
    assert stringcase.isupper(a) and stringcase.isupper(b)
    assert stringcase.isupper(a) == b
    return a ^ b
```