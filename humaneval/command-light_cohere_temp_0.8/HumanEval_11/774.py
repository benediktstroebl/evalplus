Here's a self-contained Python function that performs the string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Returns the XOR of two input strings
    a and b are only consisting of digits 1 and 0.
    """
   
    # Convert input strings to lists of integers
    a = list(map(int, a))
    b = list(map(int, b))
    # XOR operation
    result = [x ^ y for x, y in zip(a, b)]
    # Convert list back to string
    return ''.join(result)
```
This function takes two strings a and b as input and returns the XOR of these strings. 
The function converts the input strings to lists of integers, performs the XOR operation on all pairs of numbers, and then converts the resulting list back to a string.

Note that this code is self-contained, and does not require any external modules or functions.