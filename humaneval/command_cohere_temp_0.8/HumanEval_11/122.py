```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This Python script solves the problem by converting the input strings `a` and `b` to their respective binary integers using `int(a, 2)`. It then performs a binary XOR operation on these integers, converts the result back to a binary string using `bin(result)[2:]`, and returns it as the output. 

For example, given the inputs `a = "010"` and `b = "110"`, the function would correctly return `"100"` as the output.

This approach takes advantage of the binary representation of integers in Python and uses the built-in `int` and `bin` functions to perform the XOR operation efficiently without any manual conversion or parsing complications.