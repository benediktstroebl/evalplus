```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings.
    a = a[a, b]
    return ''.join(c ^ d for c, d in zip(a, b))

# Tests
assert(string_xor('010', '110')),   'First test fails'
assert(string_xor('110', '010')),   'Second test fails'
assert(string_xor('001', '01')),   'Third test fails'
assert(string_xor('11', '01')),   'Fourth test fails'
assert(string_xor('1010', '1010')),  'Fifth test passes'
print(string_xor('1010', '1010'))  # Should return '1010'
```