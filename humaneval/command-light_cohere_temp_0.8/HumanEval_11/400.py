```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b consisting only of digits 1.
    The result using binary left and right shift and bitwise XOR.
    Return result as a result as a string.
    >>> a = '010'
    b = '110'
    result = '100'
    return result

# Test cases
test_string_xor = [
    'a' = '010'
    'b' = '110'
    'result' = string_xor
    assert 'result' == '100'

    'a' = '10'
    'b' = '1'
    'result' = string_xor
    assert 'result' == '11'

    'a' = '111'
    'b' = '11'
    'result' = string_xor
    assert 'result' == '01'

    'a' = '000'
    'b' = '1111'
    'result' = string_xor
    assert 'result' == '1111'
]
``` 
This Python script defines a function `string_xor` that performs the XOR operation on two input strings, ensuring they consist only of digits 1. The script also includes a series of test cases to validate the correctness of the `string_xor` function.