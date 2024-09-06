```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters, 0 or 1.
    Perform XOR on the for each input and return the XOR'd result.
    """
    result = a[a[i] XOR b[i] for i in range(len(a))]
    return ''.join(result)
string_xor('010', '110') # 101
```