```python
def string_xor(a, b):
    return bytes(a.encode()).xor(bytes(b.encode())).decode()
```

This approach creates a bytes object from the encoded strings and applies the bitwise XOR (`xor`) operation. The result is then decoded back to a string.

Here's the accompanying Markdown code block with tests:
```python
from typing import List

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1111', '0000') == '1011'
    assert string_xor('1000', '0001') == '1101'
    assert string_xor('1100', '1010') == '0101'

test_string_xor()
```

The tests verify the function against different combinations of inputs to ensure it performs binary XOR correctly and produces the expected results.