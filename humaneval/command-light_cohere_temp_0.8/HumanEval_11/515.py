```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of ones.
    Returns: string concatenation of the binary values of '01' 
    in any order.
    """
    if not isinstance(a) or not isinstance(b):
        raise TypeError("Input must be of type string")
    return ''.join([chr(int(c)) for c in a] ^ [chr(int(c)) for c in b])
```
We use the `isinstance()` function to check if the inputs are of type `str` or not, and if not, raise a `TypeError`. We then use list comprehension to perform the XOR operation on the two input strings. The resulting characters are converted to integers and then converted back to characters. We then concatenate these strings using string concatenation `^`.