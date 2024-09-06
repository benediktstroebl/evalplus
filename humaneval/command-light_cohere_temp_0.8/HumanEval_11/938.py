```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    a: This function performs binary XOR operation on two input strings a and b.
    a and b consists only of single characters (1s and 0s).
   
    Return the XOR of a and b.
   
    Test Case:
    assert a == '010' and b == '110'
    assert string_xor('010', '110') == '100'
    assert string_xor('110', '010') == '01'
    assert string_xor('00', '01') == '10'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('1111', '0000') == '0000'
    return 'Result'
```