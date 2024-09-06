```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on inputs and return result also as a string.
    """
   
    simple cases,
    return a ^ b
    """
    return a + b

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '1') == '111'
    assert string_xor('', '') == ''
    assert string_xor('', 'a') == 'a'
    assert string_xor('a', '') == 'a'
    assert string_xor(' abc ', ' XYZ ') == ' abc  XYZ '
    assert string_xor('1010', '10') == '0110'
# Add more test cases as needed 

# main
test_string_xor()
```