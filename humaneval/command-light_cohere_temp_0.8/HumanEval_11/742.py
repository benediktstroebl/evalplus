```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings.
    return ''.join(a, b)
# Test cases
assertEqual(string_xor('1010', '1010'),'0000')
assertEqual(string_xor('010', '110'),'010000')
assertEqual(string_xor('1010', '110'),'010000')
assertEqual(string_xor('110', '010'),'010000')
assertEqual(string_xor('110', '1010'),'11000')
```