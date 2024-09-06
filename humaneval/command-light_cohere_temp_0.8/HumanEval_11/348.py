```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b.
      - Convert each string to lists of digits.
    - Perform XOR operation digit by digit
    - Convert result back to string.
    """
    string_xor('010', '110')
    # Output: 100
    """
    a = [c for c in a if c != '0']
    b = [c for c in b if c != '0']
    return ''.join([x^y for x, y in zip(a, b)])

# Test cases:
print(string_xor('010', '110'))
``` 
This Python code defines a function called `string_xor` that performs the XOR operation on two input strings. The function takes two strings a first as arguments and returns the XOR of the two strings as a single string. 

The function first converts each string to a list of its digits (only the non-zero characters), then performs the XOR operation digit by digit, and finally converts the result back to a string.