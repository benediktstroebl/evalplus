```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b and return the result as a string
    """
    return str(binxor(a, b))


def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("111", "010") == "001"
    assert string_xor("1010", "1111") == "1010"
    assert string_xor("00", "11") == "01"
    assert string_xor("000111", "1111") == "1111000111"
    assert string_xor("abcdef", "cdef") == "efcdef"
    assert string_xor("", "") == ""
    assert string_xor(" ", " ") == " "
```
This script provides a function `string_xor` that performs a binary XOR operation on two input strings and returns the result as a string. 
It also includes a set of tests that verify the correctness of this function.