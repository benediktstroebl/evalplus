```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings with only 1s and 0s.
    Returns the string a a = a ^ b
    """
    assert len(a) == len(b)
    assert all(isinstance(c, str) for c in [a, b])
    assert all(c == '0' if c == '1' else c == '1' for c in zip(a, b))
    return a ^ b

# Example
print(string_xor('010', '110'))
```
Do you want me to help you with anything else related to coding or programming?