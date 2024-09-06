```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting of only ones and zeros
    """
    return "".join([x ^ y for (x != 0) for x, y in zip(a, b)])
# Example Test
assert(string_xor('010', '110') == '100')
```