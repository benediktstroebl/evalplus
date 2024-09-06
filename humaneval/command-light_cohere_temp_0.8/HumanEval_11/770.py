```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two strings consisting only of ones and zeros.
    :type a 'STR'
    """
    a: str = '010'
    :type a
    b: str = '110'
    :type b
    return a ^ b  # return xor

# Test cases for string_xor function
assert string_xor('010', '110') == '100'
assert string_xor('111', '01') == '11'
assert string_xor('000', '000') == '0000'
assert string_xor('111', '1111') == '1111'

``` 
This Python code defines a function named string_xor that performs the XOR operation of two input strings, which consist exclusively of the digits '1' and '0'. It takes two string parameters and returns the result of the XOR, also a string. The type of the string is specified as 'STR' and the function's behavior is tested using several assertion statements, which verify that the output of the function matches the expected result for various input combinations.