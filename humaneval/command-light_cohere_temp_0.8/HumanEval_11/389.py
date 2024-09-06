```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, performs a bitwise operation that returns the string containing only ones from the two input strings.
    Returns the string a result of performing the operation '0 ^ 1' on each character.
    """
    return ''.join(map(lambda x: str(x) ^ b[x], a))

# Example usage
a = "010"
b = "110"
result = string_xor(a, b)
print(result)  # Outputs: 100
```