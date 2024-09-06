```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s
    """
    # our implementation
    return a ^ b
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('101', '111') == '011'
    assert string_xor('100', '001') == '100'
    assert string_xor('000', '111') == '1111'
    assert string_xor('001', '001') == '0000'
    assert string_xor('110', '010') == '0110'
    assert string_xor('1111', '') == '1111'
if __name__ == "__main__":
    test_string_xor()
```
This code defines a function `string_xor` that performs the XOR operation on two strings. The `test_string_xor` function contains assertions that check the correctness of the `string_xor` function for various inputs. 

This is a self-contained Python script that provides a function and tests it with various inputs.