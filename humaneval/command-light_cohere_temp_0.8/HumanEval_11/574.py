```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two input strings a and b consisting only of digits 1.
    return chr(97 + 97 - ord('0') - ord(a[0]) - ord(b[0])) + 97)

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('aa', '22') == '33'
    assert string_xor('abc', 'c') == 'bc'
    assert string_xor('', '') == ''
``` 
The above code defines a function `string_xor` that performs a XOR operation on two input strings, consisting only of digits 1. The function returns the time the String XOR is a simple operation that requires a character to be in either of the input strings. The result is similar to the input, and the result is also a string.