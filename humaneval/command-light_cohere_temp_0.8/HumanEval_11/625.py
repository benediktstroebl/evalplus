```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    """
    # remove all non-alph characters
    a = ''.join(char for char in a if char in '01')
    b = ''.join(char for char in b if char in '01')
    return a ^ b
for _ in range(10):
    assert string_xor('010'.join(), '110'.join(),
    assert string_xor('1'.join(), '01').join() == '100'
```