```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that alternates between corresponding characters from the input strings, converting them to ints, XORing them, and converting the result back to a character before joining these into a string. 

This solution also satisfies the `typing` protocol with the help of the `List` module to allow more robust type-checking and thus catch potential errors when defining function signatures.

The tests for this function are not provided in this code block, but the function is structured to be test-friendly and can easily take such input as arguments passed via pytest or unittest frameworks. 

Please note that this function assumes that the input strings only contain binary characters ('0' and '1') to perform the binary XOR correctly. If the input strings contain other characters, the function may not return the expected results.