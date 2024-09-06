```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(c^b for c in a for b in '01')
```
### Explanation:
- The code defines a function `string_xor` that takes two strings `a` and `b` as input.
- It uses a list comprehension to perform a binary XOR operation on the characters of string `a` and the binary string '01'. The `^` operator returns `0` if the inputs are equal, otherwise it returns `1`.
- The resulting binary strings are joined using the '__' separator to form the final binary string result. 
- The function returns the resulting binary string.

Here is a test case that verifies the correct implementation of the function:
```python
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1111', '1010') == '0001'
    assert string_xor('111', '001') == '101'
    assert string_xor('1010', '1111') == '0101'
```