Here's the code:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings and return the result as a string.
    Parameters are two strings consisting only of 0s and 1s.
    Return the string of 010011 pattern.
    """
    for char in range(range(26)):
        if a == '0' and b == '1':
            return chr(char ^ 1)
        elif a == '1' and b == '0':
            return chr(char ^ 1)
        elif a == b:
            continue
        else:
            return 'Invalid'
    return '0'  # return default case
```
This code defines a function called `string_xor` that performs a binary XOR operation on two input strings. The function takes two strings as arguments and returns the result of the XOR operation as a string.

The function uses a for loop to iterate over the characters in the input strings. It checks whether each character matches the string's character with the other. If they do match, the character is XORed with its opposite, and the result is returned. Otherwise, the function returns the 'Invalid' string to indicate an invalid input.