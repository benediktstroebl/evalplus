```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Returns the XOR of a and b as a string
    """
    # similar to bitwise xor operation
    # bitwise xor of two bits = 0b ^ c^d
    # becomes
    # first bit (from either a or b), if it is 1, remain 1
    # second bit, if it is 0, get reversed
    # now coming to a and b, first bit will be a
    # second bit will be b
    # so a^b = 0b
    # second bit b^a = 0a
    # put them together, we get 0a 0a
    return a ^ b
def test_xor(test_str: str) -> None:
    """ Test function
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '001'
    assert string_xor('111', '111') == '000'
    assert string_xor('abc123', 'abcd456') == '123c'
    assert string_xor('', '') == ''
``` 
Do you have any further questions about the Python code?