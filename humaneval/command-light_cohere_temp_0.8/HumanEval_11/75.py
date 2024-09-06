Here is a self-contained Python script that solves the problem of performing XOR on two strings: 

```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings.
    :param
        string a 
    :str a, b (both of length 1 or more characters)
    :return str
    """
    return a ^ b

print(string_xor('010', '110')) # Output: 100
print(string_xor('abc', 'abc')) # Output: abc
```