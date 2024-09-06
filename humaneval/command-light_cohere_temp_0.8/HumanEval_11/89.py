Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b.
    XOR operation is XOR(bits) = (b1 XOR b2) OR (b3 XOR b4) OR ...
    (b1 OR b2)
    """
    return ''.join(''.join([(ord(c) ^ ord(d)) for c, d in zip(a, b)])

# Test suite
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '110'
    assert string_xor('100', '000') == '100'
    assert string_xor('111', '111') == '0000'
    assert string_xor('0000', '1111') == '1111'

if __name__ == "__main__":
    test_string_xor()
```
The script defines a function **`string_xor`** that performs a binary XOR operation on two input strings. It then provides a test suite that checks the correctness of the **`string_xor`** function against different input pairs.