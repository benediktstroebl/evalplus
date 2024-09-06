```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR string logic operation
    """
    return "".join(sorted((a ^ b)))
a = "010"
b = "110"
result = string_xor(a, b)
print(result)  # expected output: 100
```