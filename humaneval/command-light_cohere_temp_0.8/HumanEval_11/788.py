Here is a Python script that contains a self-contained function that solves the problem of XORing two strings: 

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b, 
    return the result as a string. """
    a XOR operation is performed by taking the 
    bitwise inverse of each character in a, 
    performing a bitwise AND then XOR-ing the results together. """
    string_xor('010', '110')
    # Output: 100
    """
    a = set(a)
    b = set(b)
    return ''.join(str(i) for i in (a ^ b))
```

This script defines a function `string_xor` that performs the XOR operation on two input strings, consisting only of 1s and 0s. The function returns the important XOR value of the two strings as a single string. The XOR operation is performed by taking the bitwise inverse of each character in a, performing a bitwise AND then XOR-ing the results together.