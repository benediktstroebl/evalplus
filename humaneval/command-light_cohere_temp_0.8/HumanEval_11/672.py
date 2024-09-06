```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros
    Returns: the XOR of a and b"""
    # Convert string to lists of characters
    a = list(a)
    b = list(b)
    #XOR operation
    result = []
    for i in range(0, len(a)):
        if a[i] == '1':
            result.append(0)
        elif b[i] == '1':
            result.append(1)
        else:
            result.append(a[i])
    result = ''.join(result)
    return result

#Test case 1
print(string_xor('010', '110'))
# Expected output: 100

#Test case 2
print(string_xor('110', '010'))
# Expected output: 100

#Test case 3
print(string_xor('aa', '111'))
# Expected output: 1111
```
This code defines a function `string_xor` that performs the XOR operation on two input strings, which consist only of the characters '1' and '0'. The function converts both input strings into lists of characters and performs the XOR operation element-wise on these lists. The result is then converted back to a string and returned.