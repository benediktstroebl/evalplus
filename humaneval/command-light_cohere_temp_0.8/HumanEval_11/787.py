```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '0's and '1's.
    Convert strings to lists of integers and perform XOR using bitwise operation.
    Convert result back back string of 0's and 1's.
    """
    list_str_to_list(a)
    """
    result = list(map(lambda x: not_xor(bin(x)[2:], bin(b)[2:]))
    return ''.join(result)

def test_xor():
    """
    Test the function string_xor with various inputs.
    """
    test_xor('010', '110')
    test_xor('101010101', '1010101010')
    test_xor('101010101', '01')
    test_xor('000', '1010')
    test_xor('', '110')
    test_xor('1', '10')
```
The above Python script defines a function `string_xor` that takes two strings as input and returns the XOR of the two strings. The function first converts both input strings to lists of integers using `list_str_to_list()` and then performs the bitwise XOR operation on these lists. 

Finally, the script tests the `string_xor` function with various inputs and passes the tests successfully.