Here's the self-contained Python script with a function that performs the string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ String XOR function.
    Perform binary XOR operation on two input strings and return the result as a string.
    Args:
    a (string): First input string.
    b (string): Second input string.
    Returns:
    a (string)
    """
    return a ^ b

#Example usage
c = '010'
d = '110'
print(string_xor(c, d))
```
Do you want help with anything else?