```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros.
    return ''.join(a^[i] != b[i] for i in range(len(a)))

# Test cases
assertEqual(string_xor('010', '110'), '100')
assertEqual(string_xor('', '110'), '100')
assertEqual(string_xor('', ''), '')
assertEqual(string_xor('abc', '123'))
assertNotEqual(string_xor('111', '110'))

```