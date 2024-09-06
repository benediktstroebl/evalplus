```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two input strings composed of only digits 1 or 0.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(chr(c ^ b.map(ord(c) -10) for c in a + b) )

# Test case:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('abc', '123'))  # Input strings have mixed characters, expect error

```