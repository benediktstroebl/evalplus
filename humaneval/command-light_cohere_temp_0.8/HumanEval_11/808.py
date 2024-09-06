```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # XOR operation
    a = ''.join(c ^ b[::-1] for c, b in zip(a, b))
    return a

# Test cases
strings = [
    '010', '110', '100', '0000'
]

print(strings)
print('Result:', string_xor(*strings))
```
The function performs an XOR operation on the two input strings, and returns the result as a string.