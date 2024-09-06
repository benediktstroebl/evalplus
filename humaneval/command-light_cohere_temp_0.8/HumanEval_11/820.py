```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of '0' and '1' characters.
    return ''.join(a.join(b))
"""

# Tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '101'
    assert string_xor('1010', '0110') == '1011'
    assert string_xor('000', '1111') == '1111'

# Use the function
test_string_xor()
```