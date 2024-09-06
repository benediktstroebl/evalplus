```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two input strings.
    assert len(a) == len(b) 
    assert all(isinstance(c, str) for c in a+b)
    return ''.join(c ^ b^1 for c in a)
# example usage 
print(string_xor('010', '110')) 
```