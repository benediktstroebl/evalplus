```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    a and b can contain only single character, please
    """
    assert len(a) == 1 and len(b) == 1
    assert isinstance(a, str) and isinstance(b, str)
    return chr(97 + ord('0') ^ ord(b[0]))

# Test cases
assert string_xor('010', '110') == '100'
assert string_xor('000', '1111') == '110'
assert string_xor('111', '1111') == '000'
assert string_xor('1234', 'abc') == '2341'
```
The function 'string_xor' takes two single-character strings as input and performs a bitwise XOR operation on the characters of both strings, returning the result as a single character. 

Please note that the function also includes input validation and assert statements to ensure the input is as expected.