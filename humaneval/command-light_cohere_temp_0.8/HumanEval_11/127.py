```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings, performing a bitwise operation on each character.
    a and b are strings only of ones and zeros, with the first character of each string being the
    bit 0, and the rest being ones.
    """
    return ''.join(a.join('0')
 bitwise XOR of the first character, then the second, and so on.)
    """
    return ''.join(c if c=='0' else c^62 if c=='1' else c+32 if c=='0')

test_string = ['010', '110', '10101', '01010101', 'Are these tests passing?
# print(string_xor('010', '110'))
# print(string_xor('bibary', 'by baz'))
# print(string_xor('101010101', '1010101'))
# print(string_xor('',''))
# print(string_xor('a',''))
```