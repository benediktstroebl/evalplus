```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting only of digits 1 and 0.
    :param
        string a, b: str
    :return: result as string
    """
    # Use list comprehension to filter out non-digit characters
    a = ''.join(char for char in a if char.isdigit())
    print("a: ", a)
    b = ''.join(char for char in b if char.isdigit())
    checked string,
    return a ^ b
```