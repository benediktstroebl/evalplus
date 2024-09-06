Here's the Python script that provides a self-contained function `string_xor` that solves the problem you provided:

```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    Result is the XOR is the bitwise complement of the two inputs reversed.
    >>> string_xor('010', '110')
    '100'
    """
    return bytes([x ^ y for x, y in zip(reversed(a), reversed(b))])

def test_string_xor():
    """ Tests for the string_xor function"""
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '001'
    assert string_xor('1010', '0110') == '1001'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('5555', '1111') == '0000'
    assert string_xor('80', '7') == '64'

if __name__ == "__main__":
    test_string_xor()
```

This script provides a function `string_xor` that takes two strings as input and returns the XOR of the two input strings. The `test_string_xor` function contains several test cases to verify the correctness of the `string_xor` function. The function performs the string XOR on the reversed input strings and returns the result as a binary string.