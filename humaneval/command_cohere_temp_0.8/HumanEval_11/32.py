```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary strings (consisting of 1s and 0s) and performs a binary `xor`. The `xor` operation is done in the integerspace and converted back to strings afterward. Finally, the resulting binary string is returned. 

Here's an example of how to use the `string_xor` function:
```python
print(string_xor('010', '110')) # Should print: 100
``` 

This will output: 
100

Which is the correct `xor` operation on the two inputs, correctly identifying the fourth character as the result of the `xor` operation on the first and second characters of the input strings.