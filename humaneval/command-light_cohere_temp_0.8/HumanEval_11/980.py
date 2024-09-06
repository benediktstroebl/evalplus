```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ 
    This function performs a bitwise XOR operation on two strings, 
    and returns the result as a string.
    Args:
    a (str) : Input string consisting of only digits 0 and 1 
    / optional b = second input string.
    Returns: a string consisting of only digits 0 and 1 
    """
    return "".join([str.ord([i == '1' for i in range(len(a))) 
    for i in range(len(b))])
```