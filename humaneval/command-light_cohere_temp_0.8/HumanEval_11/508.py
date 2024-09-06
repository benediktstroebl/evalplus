```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s into a single string
    Args:
        a (str): First input string containing only digits
        b (str): Second input string containing only digits

    Returns:
        str: Resultant of XOR operation between two inputs
    """
    # Convert input strings to lists of characters
    al = list(a)
    bl = list(b)

    # XOR operation
    result = ''.join([c ^ d for c, d]) for c, d in zip(al, bl)])

    return result
```