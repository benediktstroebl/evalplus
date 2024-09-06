```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings, a and b, consisting only of 1s and 0s.
    :return: str
    :return xor(a + b[::-1])
    """
    return(a ^ b.
def_string_xor = string_xor 
# Test suite
test_suite = [
    assert_equal(def_string_xor('000', '111'),'001'),'XOR works!'
    assert_equal(def_string_xor('1010', '0110'),'1111'),'XOR fails!'
    assert_equal(def_string_xor('1010', '1010'),'0000'),'XOR still works!'
    assert_equal(def_string_xor('1010', '110'),'0110'),'XOR fails again!'
]
for t in test_suite:
    t()
```