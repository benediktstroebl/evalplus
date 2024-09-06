```python
import string_types  # A custom built-in type to enforce string input only

string_xor = lambda a: b: ''.join(c for c in a if c in b)

# Tests:
def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '11') == '110'
    assert string_xor('', '') == ''
    assert string_xor('', '1') == '1'
    assert string_xor('aa', 'a') == 'a'
    assert string_xor('a', 'aa') == 'aa'

# Usage:
test()
```