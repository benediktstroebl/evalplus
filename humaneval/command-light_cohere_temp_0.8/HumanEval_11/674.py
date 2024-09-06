```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only 1s and 0s and return the result.
    """
   
    string a = ''.join('01') + ''.join('10')
    if len(string) != len(a) + len(b):
        raise ValueError("Incorrect length for input strings!")
    ans = ''.join(c ^ d for c, d in zip(a, b))
    return ans

# Test cases
string_xor('010', '110')
string_xor('01', '10')
print(string_xor('100', '100'))
``` 
This Python script defines a function called `string_xor` that performs the XOR operation on two input strings containing only ones and zeros and returns the result as a string. It uses the test the string method to perform a list of characters and returns the result as a string.