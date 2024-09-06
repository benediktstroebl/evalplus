```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones.
    return ''.join(a ^ b)

def test_string_xor():
    assert string_xor('010', '110') == '100'

#example
print(string_xor('010', '110'))
test_string_xor()
```