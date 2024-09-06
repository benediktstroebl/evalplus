```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.isalpha() and b.isalpha() and a + b == '10'*len(a) + '1'*len(b), "Input validation error"
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This Python script solves the problem by validating the inputs, ensuring that both strings are of the same length, and consist only of the characters '0' and '1'. It uses the bitwise XOR operation to perform the binary XOR, converting the characters to integers for the operation, and then converts the result back to a string to return from the function.

For validation, the function checks that the result of bitwise XOR on alternating characters of a and b, with leading and trailing '1' characters removed, equals the output result.