```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings, performing only the operation on ones.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join_([c ^ d for c, d in zip(a, b)])

# Test the function
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '1111') == '1101'
    assert string_xor('111', '001') == '1111'
    assert string_xor('000', '1110') == '1011'
    assert string_xor('100', '110') == '1010'
    assert string_xor('0000', '1111') == '1111'

# Run the test function to check results
test_string_xor()
```