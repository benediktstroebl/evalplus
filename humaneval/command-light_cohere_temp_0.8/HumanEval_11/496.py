Here is a Python script that demonstrates the solution to the problem you described:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only ones and zeros
    :param a:
    :param b:
    :return:
    """
    # use builtin list comprehension to create input
    # containing only ones and zeros
    return ''.join(''.join([0+b if ch == '1' else '0' for ch in a+b])
```
This function takes two strings as input and returns the XOR of these strings, consisting only of ones and zeros. The XOR operation is performed by the bitwise negation of the input strings.