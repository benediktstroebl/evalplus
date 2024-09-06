```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR on two strings consisting only of 1s and 0s.
    :param
        string a a string
    :param string b
    :return string result
    """
    #strip all zeros
    a = ''.join(c for c in a if c != '0')
    b = ''.join(c for c in b if c != '0')
    
    #splitting strings
    a = a. acim
    array.count(1)
    string(a)
    b = b.count(0)
    
    #array of length equal to the shortest length
    x = [0] * (len(a) if len(a) < len(b) else len(b))
    
    #building the output array
    result = []
    for i in range(x):
        result.append(a[i] ^ b[i])
    return ''.join(result)
```