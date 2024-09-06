```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The function uses `typing.zip` to iterate over the characters of both strings and calculates the XOR using `^` operator. The result is then joined into a single string without any separators and returned.

The test cases are not included in this markdown code block but are required to ensure the function behaves as expected. These tests could cover edge cases such as handling an odd-length string, where the last character will be auto-appended with a 0. These tests can be added separately to validate the function and ensure it behaves as expected.