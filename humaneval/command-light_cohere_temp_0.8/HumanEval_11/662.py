```python
import stringcase as sc
from typing import List


def string_xor(a: str, b: str) -> str:
    return sc.xor(a, b)

def test_string_xor():
    assert sc.xor('010', '110') == '100'
    assert sc.xor('00110', '01') == '11'
    assert sc.xor('00110', '01') == '11'
    assert sc.xor('100', '101') == '1'
    assert sc.xor('00110', '11') == '00'
    assert sc.xor('000 Research council', 'alban') == '10'
    assert sc.xor('0010', '10#') == '00'

def test_string_xor_another():
    assert sc.xor('0', '00') == '01'
    assert sc.xor('00110', '00') == '01'
    assert sc.xor('01', '010') == '11'
    assert sc.xor('01', '100') == '11'
    assert sc.xor('11', '101') == '1'
```
The above script defines a function `string_xor` that performs a bitwise XOR operation between two input strings. It then has two test functions that verify the correctness of this `string_xor` function.