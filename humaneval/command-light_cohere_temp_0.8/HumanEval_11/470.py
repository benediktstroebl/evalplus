```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings, a and b, consisting only of single characters.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(*[0 ^ char for char in a] + [0 ^ char for char in b])

test_string = ['010', '110', '00110', '001']
test_result = string_xor(*test_string)
assert test_result == '100'
```