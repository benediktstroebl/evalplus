```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only digits 1 and 0.
    and return the strings only
    """ input as a string
    """
    return ''.join(c ^ d for c, d in zip('0' * len(a), '0' * len(b)))
# Example usage:
print(string_xor('010', '110'))
```
This function performs a binary XOR operation on two strings, which only contain digits 1 and 0, and returns the result as a string. It's self-contained, and does not require any external variables.