```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings, and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return str(bin(ord(a[0]) ^ ord(b[0]))[2:])
# Tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '110') == '00'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('111', '110') == '00'
    assert string_xor('1111', '0000') == '1111'
    assert string_xor(' Language ', ' Blissful ') == 'LSBLFSH'
# main
if __name__ == "__main__":
    test_string_xor()
``` 
The above code defines a function string_xor that performs a binary XOR operation on two input strings. The function takes two strings as arguments and returns the result as a string. The function uses the string representation of the binary XOR operation and returns the result accordingly. The test_string_xor function is used to test the functionality of the string_xor function with a variety of inputs.