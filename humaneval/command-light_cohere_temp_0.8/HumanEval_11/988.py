```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two input strings consisting only of '0's and '1's.
    - 'a' and 'b' are expected to be strings containing only '0's and '1's.
    - Perform XOR bit by bitwise AND on the two input strings and return result.
    - Test if both strings contain only '0's and '1's, the XOR should return '0'.

    #Test cases
    assert string_xor('010', '110') == '100'
    assert string_xor('00', '11') == '01'
    assert string_xor('1010', '1111') == '1010'
    assert string_xor('1010', '10') == '0110'
    assert string_xor('1010', '110') != '1010'
```