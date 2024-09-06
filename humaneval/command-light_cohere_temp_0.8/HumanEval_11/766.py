```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b, 
    a and b can only consist of only '0' and '1' characters.
    Returns the string that is constructed by concatenating a and b, 
    and converting it to lowercase.
    """
    return a a+b+b[-1:]
# Example usage:
print(string_xor('010', '110'))  # Output: 100
```