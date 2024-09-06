```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return the result as a string.
    :
    
    a = a ^ b
    result = ''.join(''.join(c ^ d for c in b) for c, d in zip(a, b))
    return ''.join(result)

# Test case function
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('q', 'w') == 'y'
    assert string_xor('000', '11') == '001'
    assert string_xor('', '') == ''
    assert string_xor('a', 'b') == 'ab'
    assert string_xor('aa', 'a') == 'aaa'
```
This script defines a function string_xor that performs a XOR operation on two input strings and returns the result as a string. It also includes a test case function test_xor that provides several input combinations and asserts the output of the string_xor function.