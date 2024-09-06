```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of ones and zeros.
    :return:: the string concatenation of all characters in which appeared first in a and b but not in either input.
    """
    string_xor('010', '110')
    """
    result = ""
    for char in min(a, b):
        if char == char.upper():
            result += char
        }
    return result
```  This function performs a XOR operation on two input strings, a and b, and returns the result as a string. The function uses the string concatenation to create the result, which is also a string consisting of all characters from the first input string (a) and the second input string (b) that were not present in either of the inputs.