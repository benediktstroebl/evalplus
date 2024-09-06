```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of digits 1-9
    Perform binary XOR operation on these inputs and return result as a string.
    """
    XOR = "0"*(len(a)+len(b))
    return ''.join(*((ord(c)^(ord(d))) for d,c in zip(a,b)))

# Test case:
print(string_xor('010', '110'))
``` 
Do you want help with anything else with Python, coding or any specific topic you'd like to explore further?