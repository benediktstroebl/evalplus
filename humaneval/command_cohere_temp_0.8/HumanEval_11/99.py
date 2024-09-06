```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(c^b for c in a for b in '01')
```
### Test Cases
```python
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '1101') == '1001'
    assert string_xor('1111', '1111') == '0000'
    assert string_xor('111', '1101') == '0001'
    assert string_xor('1100', '00011011') == '001001'
```