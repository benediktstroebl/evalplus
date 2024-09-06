```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR string a and b """
    return a ^ b

def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '111'
    assert string_xor('111', '11') == '111'
    assert string_xor('100', '00') == '100'
    assert string_xor('000', '111') == '000'
    assert string_xor('1111', '1') == '1111'

# Driver code
if __name__ == "__main__":
    test_xor()
```
This code has a function called string_xor that performs the XOR operation on two input strings. The test_xor function contains a series of assertions that verify the correctness of the string_xor function. The main code ensures that the test_xor function is run when the script is executed.