```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    'a' and 'b' are two strings, each consisting only of 1s and 0s.
    XOR operation is string in the format 'a[0:]'
    :type a: str
    :type b: str
    :rtype: str
    """
    return a ^ b

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '111'
    assert string_xor('00001111', '1010') == '00001100'
    assert string_xor('1111', '01111') == '00000111'

if __name__ == "__main__":
    test_string_xor()
```
This script defines a function `string_xor` that performs a XOR operation on two input strings, both consisting only of 1s and 0s. The XOR operation is then a simple concatenation of the two strings with a '^' character in between. The tests provided ensure that the function is working correctly.