```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(x ^ y for x, y in zip(a, b))
```

The code uses Python's typing module to improve type safety and also uses a generator expression (via `zip`) to streamline the XOR operation and string concatenation (`__join`). The resulting code is more efficient and readable. 

This solution assumes that the input strings, `a` and `b`, only contain the characters '0' and '1'. If the input strings contain other characters, the solution may produce unexpected results.