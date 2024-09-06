```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function performs binary XOR operation on two strings.
   : return ''.join([c ^ d for i in range(len(a)) for c,d in zip(a,b)])
    """
    return "".join([c ^ d for i in range(len(a)) for c,d in zip(a,b)])
# Example test cases
a = "010"
b = "110"
print(string_xor(a,b)) # Output: 100
```