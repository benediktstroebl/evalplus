```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings, a and b, consisting only of 1s and 0s.
    Returns the string-like strings and returns the XOR result as a string.
    """ 


    a = "".join(*a)
    b = "".join(*b)
    return "".join([x ^ b for char in range])

# Example Test
a = "010"
b = "110"
result = string_xor(a, b)
print(result) # Output: 100
```