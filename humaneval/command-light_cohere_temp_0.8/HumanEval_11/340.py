```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros
    Returns: the XOR of a and b
    """
    return sum((int ^ int(b[i])) for i,instr in enumerate(a))
# Example usage
a = "010"
b = "110"
result = string_xor(a, b)
print(result) # Output should be "100"
```