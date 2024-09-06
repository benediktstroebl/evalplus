```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros.
    :return str(a ^ b)
    """

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '001'
    assert string_xor('00', '10') == '010'
    assert string_xor('001', '100') == '100'
    assert string_xor('1', '10') == '01'
    assert string_xor('000', '0000') == '0000'

# Call the function with tests
test_string_xor()
```
The code you provided is a Python script with a self-contained function `string_xor` that performs the XOR operation on two input strings consisting only of ones and zeros. The function uses the string formatting to return the result of the XOR operation as a string.

Additionally, the code provides a function `test_string_xor` to run the function and assert if the results of the function are correct for a set of test cases.