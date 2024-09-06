```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function performs binary XOR operation on two strings consisting only of ones and zeros.
    : Return the general implementation using only single character input
    """
    # Convert to list of integers, ensuring all zeros are removed
    a = ''.join(int(c) for c in a)
    b = ''.join(int(c) for c in b)

    # XOR two integers
    result = a ^ b

    # Convert back to string
    return ''.join(chr(result))

def test_string_xor():
    """ Test case function to check the correctness of the xor function
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '011'
    assert string_xor('000', '111') == '111'
    assert string_xor('1001', '0') == '1000'
    assert string_xor('1010', '1') == '1001'
``` 
The above Python script defines a function `string_xor` that performs the XOR operation on two input strings. It also has a test case function that verifies the correctness of the `string_xor` function.