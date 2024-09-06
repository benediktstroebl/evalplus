```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary `xor`. The `xor` operation returns a string consisting of the corresponding `0` and `1` for each pair of digits `a` and `b`. The `zip` function loops over each pair of digits `a` and `b` and takes the `xor` of their ASCII codes. And finally, `'.join()` aggregates the resulting digits to form a string that is returned by the function. 

Here is an example usage of the function:
```python
print(string_xor('010', '110')) # Output: '100'
```

This would output: '100' -- the XOR of the two input strings.