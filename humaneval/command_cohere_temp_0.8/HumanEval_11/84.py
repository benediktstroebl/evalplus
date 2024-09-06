```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return str(int(a, 2) ^ int(b, 2))
```

The `string_xor` function takes two strings `a` and `b` as input, each representing binary numbers in base-2 notation. It employs the `^` operator, performing binary XOR on the underlying integers represented by these strings. The result of the operation is then converted back to a string format and returned as the output. 

This function elegantly solves the problem in a self-contained manner, ensuring it can be understood and used without relying on additional dependencies or external code.