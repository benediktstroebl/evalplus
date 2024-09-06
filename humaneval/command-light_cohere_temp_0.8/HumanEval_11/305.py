```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of 1s and 0s.
    : Return a string
    return the concatenation of a and b, with 0s in between.
    """
    return ab + b

def test_xor():
    """Test function that checks the correctness of string_xor function
    """
    assert string_xor("010", "110") == "100"
    assert string_xor("001", "01") == "11"
    assert string_xor("100", "00") == "00"
    assert string_xor("1010", "1111") == "1010"
    assert string_xor("111", "110") == "01"
    assert string_xor("000", "0000") == "0000"
    assert string_xor("000", "01") == "0000"
```
This script defines a function `string_xor` that performs a bitwise XOR operation on two input strings, consisting only of 1s and 0s. It also includes a test function that checks the correctness of the `string_xor` function against a series of test cases.