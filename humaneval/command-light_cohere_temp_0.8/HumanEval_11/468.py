```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    Result = sum(sorted(a^b))
    """
    return str(sum(sorted(a ^ b)))
# Example:
a = '010'
b = '110'
result = string_xor(a, b)
print(result) # Output: 100
```