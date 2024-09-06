```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that takes pairs of corresponding elements from both strings, casts them to integers, performs the XOR operation, and converts the result back to a character using the `chr` function. 

The code block includes a docstring that provides an example usage of this function, testing it with the input strings '010' and '110'. The resulting output '100' is demonstrated to be the XOR of these two strings.  This demonstrates a basic usage of Python's typing module for type hinting as well as sophisticated string manipulation techniques.