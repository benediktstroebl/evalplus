```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '1' and '0' characters.
    """
   
    function XOR and returns the result.
    """
    code 
    """
    There is a self-contained and efficient function that takes two strings as arguments, performs the XOR operation, and returns the result as a string.
```
def string_xor(a: str, b: str) -> str:
    result = ""
    for ch in a + b:
        if ch == "1":
            result += int(ch) << 1
        else:
            result += int(ch)
    return result
```