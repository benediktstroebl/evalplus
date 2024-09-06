```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function performs XOR operation on two strings containing only digits 1 and 0.
    Returns the XOR with a and b
    """
    return str(int("".join(c) ^ int("".join(d)) for c, d in zip(a, b)))

# Test
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("11", "01") == "10"
    assert string_xor("1000", "1111") == "0"
    assert string_xor("00000000", "00000000") == "1111111111"
    assert string_xor("00001111", "00001111") == "111111111"
    assert string_xor("01", "10") == "11"
    assert string_xor("00", "00") == "0000"
    assert string_xor("000", "111") == "11"

if __name__ == "__main__":
    test_string_xor()
``` 
This script defines a function `string_xor` that performs a binary XOR operation on two input strings. The function uses the XOR on each character of the input strings using bitwise XOR operation (`^`) and converts the result back to a string. The test function contains several tests to verify the correctness of the `string_xor` function.