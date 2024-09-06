```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that takes pairs of corresponding elements from both strings, converts them to integers, performs the XOR operation, and then converts the result back to a character using the `chr` function. 

The `typing` import establishes the proper type signature for the function, ensuring that the function can accept only two parameters of type `str` and return a value of type `str`. 

This solution provides a straightforward way to perform binary XOR on two strings and return the result as a string, as required by the provided test case.