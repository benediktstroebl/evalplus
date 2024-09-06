```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings,
    performing only binary operations with '1' and '0'.
    """
    result = ""
    for c in a + b:
        if c == '1':
            result += '0'
        elif c == '0':
            result += '1'
    return result

# Test suite for the function
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '101'
    assert string_xor('111', '110') == '011'
    assert string_xor('1000', '1001') == '0000'
    assert string_xor('1010', '1011') == '1101'
    assert string_xor('1110', '1010') == '1011'
# Run the test suite when the function is called
test_string_xor()
```