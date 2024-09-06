```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings using only ones and zeros
    """
    # Ensure both inputs are converted to lists of integers
    a = [int(c) for c in a]
    b = [int(c) for c in b]
    # XOR two lists of integers
    return ''.join([x ^ y for i, j in zip(a, b)])
# Tests
string_xor('010', '110')
# Expected Output: 100
string_xor('abc', '!'^)
# Expected Output: !c
```