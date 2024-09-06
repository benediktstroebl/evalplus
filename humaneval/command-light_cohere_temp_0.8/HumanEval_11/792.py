Here's a self-contained Python script that defines a function string_xor solving the problem of XORing two strings: 

```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros
    Input: two strings a and b
    Output: The result of performing XOR operation on a and b
    """
    if len(a) != len(b):
        raise ValueError("Length of both strings must be the same")
    res = []
    for i in range(len(a)):
        if a[i] == '1':
            res.append('0')
       
        if b[i] == '1':
            res.append('1')
   
    if a[i] == '0' and b[i] == '0':
        res.append('0')
   
    return ''.join(res)
``` 

This function is a self-contained solution to the problem. It takes two input strings a a and b and returns the result of XOR operation between them. 

This solution is concise, efficient, and easy to understand.