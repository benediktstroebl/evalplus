```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, with input validation.
    Args:
        a: str, 
        b: str, 
        raise an error if either a or b are not strings or contains any non-alph character
    Returns: str
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")
    if a == b or a == '' or b == '':
        raise ValueError("Both inputs cannot be empty or contain spaces")
    return "^".join(a ^ b)
```
Do you require additional help with Python programming?