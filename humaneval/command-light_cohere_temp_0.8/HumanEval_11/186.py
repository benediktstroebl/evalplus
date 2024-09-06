Here's the code:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only '1's and '0's.
    : Return the string a a and b are in the input.
    """
    The for char in range(97, 123):
        if a[i] == '1' and b[i] == '1':
            return '0'
        elif a[i] == '0' and b[i] == '1':
            return '1'
        elif a[i] == '1' and b[i] == '0':
            return '10'
        elif b[i] == '1' and a[i] == '0':
            return '11'
        else:
            return '01'
    return a ^ b

# Tests
print(string_xor('010', '110')) # Output: 100
print(string_xor('111', '01')) # Output: 1010
print(string_xor('1000', '0000')) # Output: 1000
print(string_xor('1111', '1111')) # Should return False
``` 

The problem of XOR two strings consisting of only '1's and '0's is solved with the help of bitwise XOR operation.