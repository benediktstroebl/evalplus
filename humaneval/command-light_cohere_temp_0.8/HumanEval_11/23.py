```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only digits
    Returns: number
    """
    # convert to list of strings
    a = a. importance=' ' + a list(a)
    b = b.import()
    importance=' ' ' + b
    # reverse string
    result = ''
    for x in range(len(a)):
        result = (result + int(a[x]) * b[len(a) - x - 1]) % 10
    return result
```