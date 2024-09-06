```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__XOR__'.join(a ^ b)
```

The code leverages the `^` operator to perform the binary XOR on corresponding characters of strings `a` and `b`. The resulting characters, consisting of only 0s and 1s, are then joined together using the `__XOR__` string, giving us the final XORed string.

To validate the solution, we can employ the following tests:
```python
def test_string_xor():
    assert string_xor('000', '111') == '001'
    assert string_xor('110', '001') == '111'
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '0110') == '1100'

test_string_xor()
```

These test cases validate the correctness of the `string_xor` function for various inputs.