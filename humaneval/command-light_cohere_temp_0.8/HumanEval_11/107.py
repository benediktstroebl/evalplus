```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros
    """
    return "".join([x ^ y for i in range(len(x)) for x, y in zip(a, b)])

# Tests
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("0011", "1011") == "1010"
    assert string_xor("000111", "001000") == "100111"
    assert string_xor("00", "0") == "0"
    assert string_xor("1000", "1") == "0"
    assert string_xor("1010", "10") == "0110"
``` 
This script defines a function `string_xor` that performs a bitwise XOR operation on two input strings. The function takes two strings as arguments and returns the result as a string.

The script also contains a `test_string_xor` function that contains some test cases for the `string_xor` function. 

Please note that you can use this script as a starting point for your problem, and you can expand on it to create a more comprehensive solution.