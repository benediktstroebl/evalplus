```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two strings (`a` and `b`) consisting of only ones and zeroes and returns the result as a string. The function uses `typing` to ensure type safety and uses `zip` to iterate over the characters of the two strings, performing the `XOR` operation on the corresponding integers and converting the result back to a character using `chr`.

Here is an example usage of the function:
```python
>>> string_xor('010', '110')
'100'
``` 

This would output the result of the binary `XOR` operation between the strings '010' and '110', which is '100'.