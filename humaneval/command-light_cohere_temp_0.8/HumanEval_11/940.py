```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters, returns their XOR.

    :
    binary_xor(0,1) == 1
    :return "0"
    """
    if a == "0" and b == "1":
        return "1"
    elif a == "1" and b == "0":
        return "0"
    else:
        return "0"

# Tests
string1 = "00"
string2 = "11"
assertEqual(string_xor(string1, string2), "1")
string3 = "01"
string4 = "10"
assertEqual(string_xor(string3, string4), "0")
```