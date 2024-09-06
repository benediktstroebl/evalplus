```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that performs binary `XOR` on two strings (`a` and `b`) consisting of only `0`s and `1`s. It accomplishes this by using the `zip` function to pair the characters of both strings and converting them to integers for XOR operation, finally converting the result back to a character for string concatenation. 

The function is tested using the `>>> ` syntax to call the function with two example strings, and the result is checked against the expected output.  This provides an opportunity to evaluate the function and its behavior, ensuring it aligns with the problem's requirement to return the binary XOR of two provided strings.  If the result is incorrect, the function's implementation can be adjusted accordingly, aiding in troubleshooting and refinement.