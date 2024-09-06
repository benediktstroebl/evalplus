```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings a and b consisting only of 1s and 0s.
    - Convert input strings to lists of characters
    - XOR the corresponding characters
    - Convert the result back to a string.
    return ''.join(result)
a = "01010"
b = "100110"
print(string_xor(a, b))  # Output: 100
a = "0000"
b = "111111"
print(string_xor(a, b))  # Output: 11
```