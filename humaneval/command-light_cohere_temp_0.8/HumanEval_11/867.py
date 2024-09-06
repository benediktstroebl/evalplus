```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only digits 1 and 0.
    Result: 1010 """
    return a ^ b

# Test suite
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("00", "10") == "000"
    assert string_xor("111", "01") == "110"
    assert string_xor("000", "0000") == "0000"
    assert string_xor("1111", "1111") == "0000"
    assert string_xor("1010", "1010") == "0110"
    assert string_xor("1000", "001000") == "00000"
    assert string_xor("1010", "1") == "0110"
    assert string_xor("00", "") == ""

if __name__ == "__main__":
    test_string_xor()
```
This Python script defines a function `string_xor` that performs a bitwise XOR operation between two input strings, both consisting only of the digit '1'. The function returns the result of the XOR operation as a string.

It also includes a test suite with several test cases that validate the functionality of the `string_xor` function. The `test_string_xor()` function checks the correctness of the function by asserting that the output of the function is correct for a variety of input strings. 
Finally, the script runs the test suite to ensure the function's correctness.