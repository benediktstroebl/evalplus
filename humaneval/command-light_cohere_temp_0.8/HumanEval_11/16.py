```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '0' and '1'.
    :param a: str, first string
    :param b: str, second string
    :return: str, result of XOR operation
    """
    # convert string to list of characters
    a = ''.join(a)
    b = ''.join(b)
    #XOR
    result = [0 for i in range(len(a))]
    for i in range(len(a)):
        result[i] = a[i] ^ b[i]
    return ''.join(result)
```
This Python function takes two strings a and b as input, consisting only of 0's and 1's, and performs the XOR operation on those strings. The function then converts both strings to lists of characters, and iterates through each character in both strings. The XOR operation is then performed by negating each character in b and adding the result to the corresponding character in a. one a list comprehension that result, which is the desired XOR operation. The function then returns the string that contains the result of the XOR operation on the two input strings.