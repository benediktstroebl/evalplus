```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings composed only of ones and zeros.
    Perform binary XOR on these inputs and return result also as a string.
    """
    generate an XOR between a and b and return the result.

def test_string_xor():
    # Test case 1
    assert string_xor('010', '110') == '100'
    # Test case 2
    assert string_xor('111', '110') =='101'
    # Test case 3
    assert string_xor('010', '01') =='100'
    # Test case 4
    assert string_xor('11', '0111') =='100'
    # Test case 5
    assert string_xor('001', '100') =='01'
    # Test case 6
    assert string_xor('1010', '10') =='01'
    # Test case 7
    assert string_xor('1', '01') =='10'
    # Test case 8
    assert string_xor('000', '10') =='00'
    # Test case 9
    assert string_xor('000', '01') =='00'
    # Test case 10
    assert string_xor('1010', '110') =='100'

test_string_xor()
```