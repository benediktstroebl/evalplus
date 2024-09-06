```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only ones and zeros
    Returns the XOR result as a string.
    """
    a list of characters, we will use slicing to create two lists
    'a' contains only ones and 'b' contains only zeros. Then we apply bitwise XOR and convert it to a string.
    """
    create a list of characters from the input strings
    a = [c for c in a]
    b = [c for c in b]
    return ''.join(a XOR b)
    """

def test_string_xor():
    """
    Test the string_xor function with various inputs
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('0011', '1111') == '0000'
    assert string_xor('', '') == ''
    assert string_xor('101010', '10') == '01000'
    assert string_xor('101010', 10) == '10010100'
    assert string_xor('10101010', 10) == '1001010100'
    assert string_xor('', '0') == '0'
    assert string_xor('10101010', '101010') == '1001101010'

if __name__ == "__main__":
    test_string_xor()
``` 
This script defines a function `string_xor` that performs the XOR operation on two input strings, and a test function `test_string_xor` to check the correctness of the function with various inputs. 
It then passes the test function to check if the `string_xor` function is working correctly.