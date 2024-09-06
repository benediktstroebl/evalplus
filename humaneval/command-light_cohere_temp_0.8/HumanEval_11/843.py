```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    """
    process
   
    a, b into lists of ones and zeros respectively,
    then return their XOR.
    """ 
    ones = list(a) ^ list(b)
    zeros = list(set(a) ^ set(b))
    return "".join(ones + zeros)

# Unit tests
strings = [string_xor('010', '110'),
string_xor('1010', '1010'),
string_xor('110', '010'),
string_xor('0011', '1111'),
string_xor('1010', '1110')]
print(strings)
```