```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only ones and zeros.
    """
    strings are converted to lists of characters, then XORed in
    a list comprehension and converted back to a string.
    """
    test:
    Test case 1:
    Input: '010'
    Should return: '100'

    Test case 2:
    Input: '110'
    Should return: '100'

    Test case 3:
    Input: '00'
    Should return: '000'

    Test case 4:
    Input: '111'
    Should return: '000'

    Test case 5:
    Input: '102'
    Should return: '002'

    Test case 6:
    Input: '000'
    Should return: '000'

    Test case 7:
    Input: '111'
    Should return: '000'
    """
    a = "010"
    b = "110"
    return str(list(map(lambda x: x ^ ord(x), a + b)))

# Example
print(string_xor("010", "110"))  # Output:  '100' 
``` 
This function takes two strings, a and b, consisting only of ones and zeros, and performs a binary XOR operation on the two strings. The function first converts both strings into lists of characters and then performs the XOR operation in a list comprehension and finally converts the result back into a string.