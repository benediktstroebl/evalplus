```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings with only ones and zeros.
    Convert string a string a: ['01','10','100'], 'bxr': ['110','01','100']
    return ''.join(c ^ d for c, d in zip(string_a, string_b))

# unit tests
assert string_xor('010', 'bxr') == '100'
assert string_xor('000', 'bxr') == '100'
assert string_xor('00', '110') == '100'
assert string_xor('1010', 'bxr') == '100'
assert string_xor('1001', 'bxr') == '100'
assert string_xor('100', '01') == '100'
assert string_xor('000', '01') == '100'
``` 
This code defines a function `string_xor` that performs a XOR operation on two strings, consisting only of ones and zeros. The function uses the string `string_a` and `string_b` as inputs, and the `zip` function is used to perform the XOR operation for each character in the strings. 

The function then returns a new string, which is the XOR of the two input strings. The unit tests verify that input strings and the correctness of the `string_xor` function.