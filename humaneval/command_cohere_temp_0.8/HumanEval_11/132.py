```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that alternates between characters from both strings, taking their ASCII values, doing a binary XOR on these values, and converting the result back to a character.

This solution does not conform to the specified typing information, as it missing types for the return value and the zip argument. Also, the old `chr` function has been replaced by `bytes.decode` for creating strings from ASCII values since Python 3. Here is the full code:
```python
from typing import List, Union

def string_xor(a: str, b: str) -> str:
    return bytes(x ^ y for x, y in zip(a.encode(), b.encode())).decode()
``` 

This code should be compatible with the newest Python versions while preserving the functionality and the problem solution.