```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses `typing.zip` to iterate over the characters of both strings, performing binary XOR on the corresponding characters using `int(x) ^ int(y)` and converting the result back to a character using `chr`. The resulting XORed string is then returned as a single string using `'.join'` function. 

Such usage of `typing` module helps to make code more readable and provide type hints for better code understanding and maintainability. 

This solution is self-contained and can be easily executed independently to test its functionality. 

**NOTE**: This solution assumes that both input strings only consist of digits '0' and '1'.