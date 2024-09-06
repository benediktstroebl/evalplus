```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only 1s and 0s.
    return sum((c ^ d) for d in zip(a, b))
a = '01010'
b = '01010110'
print(string_xor(a, b))  # Expected Output: 100
```