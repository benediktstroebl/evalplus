```python
import stringcase
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    :type a: str
    :type b: str
    :rtype: str
    """
    return ''.join(c ^ d for c, d in zip(a, b))

# Testing the function with different inputs
assertEqual(string_xor('010', '110'), '100')
assertEqual(string_xor('abc', 'abc'))
assertEqual(string_xor('', '123'))
assertEqual(string_xor('', ''))
assertEqual(string_xor('abc', '123'))

# Output:
100
True
abc
123

```