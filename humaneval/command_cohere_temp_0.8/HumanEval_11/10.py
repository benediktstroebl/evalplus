```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary XOR on two input strings `a` and `b`, taking them as arguments. It uses `typing` to ensure type safety and employs a list comprehension to efficiently calculate the XOR of corresponding bits from the input strings. 

To use this function, you can call it with two strings containing only 0s and 1s, and it will return the binary XOR of these strings as a string. 

For example:
```python
print(string_xor('010', '110'))  # Output: '100'
```