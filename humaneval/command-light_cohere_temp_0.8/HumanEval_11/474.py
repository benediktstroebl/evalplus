```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Inputs are two strings a and b consisting only of single characters (1s and 0s).
    Perform XOR operation and return the result.
    >>> string_xor('010', '110')
    '100'
    """
    # Use list comprehension to convert input strings into lists of characters
    a = ['0'] + a.
    b = ['0'] + b
    # Use XOR operation to combine characters in lists
    return ''.join([1 if x != y else 0 for x, y in zip(a, b)])
# Unit tests:
#   Test with known good inputs/outputs
#   1.string_xor('010', '110')
#   2.string_xor('001', '1')
#   3.string_xor('000x', '10')
#   4.string_xor('001', '01')
#   5.string_xor('000 certain', '110')
```