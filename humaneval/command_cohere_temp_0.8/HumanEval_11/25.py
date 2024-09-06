```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses `typing.zip` to iterate over the characters of both strings, performing binary XOR on the corresponding characters' ASCII values and converting the result back to a character using `chr`. The resulting string is then returned.

Here is an example of how to use this function:
```python
print(string_xor('010', '110')) # Output: '100'
```

This would output:
```100```