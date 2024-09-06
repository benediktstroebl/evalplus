```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    '0' <= a <= '10' and '0' <= b <= '10'
    """
    assert 0 <= a <= '10' and 0 <= b <= '10',
    return str(int("100" ^ (ord(a) ^ ord(b))))

print(string_xor('010', '110')) # Output: 100
```