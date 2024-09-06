```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings,
    Expects inputs a and b to only contain characters '0' and '1'.
    Returns the result as a string.
    """
    string_xor('010', '110')
    '100'
    assert string_xor('000', '111') == '110'
    assert string_xor('111', '000') == '01'
    assert string_xor('111', '111') == '000'
    assert string_xor('111', '10') == '1'
    assert string_xor('000', '01') == '1'
    assert string_xor('111', '') == '1'
    return '0'
```