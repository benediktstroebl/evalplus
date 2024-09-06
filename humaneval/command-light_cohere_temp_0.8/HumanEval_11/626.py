```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s.
    return ''.join(a[i] ^ b[i] for i in range(len(a)))
    """
    return ''.join(a[i] ^ b[i] for i in range(len(a)))

# Test cases
string_xor('010', '110')
# Expected Output: 100
string_xor('001', '0')
# Expected Output: 000
string_xor('0011', '0011')
# Expected Output: 000
string_xor('1010', '1011')
# Expected Output: 101
```
This script defines a function `string_xor` that performs a bitwise XOR operation on two input strings consisting only of '1's and '0's, and returns the result as a string. 

It uses the `join.join` function to slice the bits of the input strings and performs the XOR operation on each slice.