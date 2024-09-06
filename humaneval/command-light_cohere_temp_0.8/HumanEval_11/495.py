```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on the inputs and return result as a string
    """
    return "".join([c ^ d for c, d in a + b])
a = "010"
b = "110"
result = string_xor(a, b)
print(result)  # Output: 100
``` 
This script defines a function `string_xor` that takes two strings a and b as input and performs the binary XOR operation on them, returning the result as a string.