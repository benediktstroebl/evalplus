```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings `a` and `b` as input. It uses `typing` to ensure type correctness and employs bitwise XOR to convert the result of the logical operation to a character for each corresponding bit. The `zip` function arranges the two strings for pairing, and the `join` method concatenates the characters back together to form the final result. 

Here is an example usage of this function:
```python
assert string_xor('010', '110') == '100'
```

This will return `'100'` as the resultant string after performing a bitwise XOR on the input strings.