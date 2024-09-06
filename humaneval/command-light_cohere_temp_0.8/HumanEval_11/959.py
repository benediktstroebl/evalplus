```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings using bytes.
    a string consists only of characters [0-9]
    """
    assert len(a) == len(b)
    assert all(c in '01' for c in a + b)
    return bytes.join(a ^ b)

def test_string_xor():
    """ Test case function, checks if returned string is valid """
    assert '100' == string_xor('010', '110')
    assert '000' == string_xor('111', '010')
    assert '0000' == string_xor('000', '00')
    assert '0000' != string_xor('1111', '1010')

# Call the test function to run the tests
test_string_xor()
```