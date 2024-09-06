```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only '0's and '1's
    Returns: 010101...
    """
    return sum((x ^ y) for x, y in zip(a, b))

# Test cases
assert string_xor('010', '110') == '100'
assert string_xor('001', '01') == '11'
assert string_xor('1010', '1010') == '101'
assert string_xor('1010', '0110') == '11000101'
assert string_xor('00', '10') == '01'
assert string_xor('1111', '11') == '00001111'
```
This code defines a function `string_xor` that performs the XOR operation on two input strings, both consisting of only the digits '0' and '1'. The function returns the result of the XOR operation as a string.

The test cases ensure that the function works correctly for various input combinations.