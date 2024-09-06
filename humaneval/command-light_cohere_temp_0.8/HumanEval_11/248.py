```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings consisting only of digits 1 and 0.
    Returns the pattern XOR operation, XOR of two input strings, a and b. XORing as a string a concatenation of the input strings.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(c if c in a else c in b else c for c in (a + b))

# Test suite
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('11', '01') == '10'
    assert string_xor('111', '0') == '11'
    assert string_xor('00', '00') == '00'
    assert string_xor('1010', '10') == '01'
    assert string_xor('11111', '1111') == '0000'

if __name__ == "__main__":
    test_string_xor()
```
This code defines a `string_xor` function that performs a XOR operation on two input strings consisting only of the digit '1' and performs a test suite that includes various inputs and asserts that the output of the `string_xor` function matches the expected result for each input.