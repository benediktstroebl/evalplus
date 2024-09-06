```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of '0's and '1's.
    Parameters:
        a and b are strings consisting only of '0' and '1'.
    return a ^ b
for _ in ['00', '10', '01']:
    assert string_xor(_ ,_ ) == _
    for _ in ['100', '101', '1000']:
        assert string_xor(_ ,_ ) == _
```