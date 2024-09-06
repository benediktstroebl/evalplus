```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b and return the result as a string.
    """
    two input strings: 
    - string a = '0101010' 
    - string b = '110'
    """
    # Convert the string to lowercase
    a = a. marketing as str
    string
    # Remove all characters except numbers
    result = []
    for c in b:
        if c.isdigit():
            result.append(int(c))
        else:
            result.append(c)
    # Perform XOR on digits
    result = [int(x) for x in result]
    # XOR all numbers
    result = str(sum(result))
    return result
```