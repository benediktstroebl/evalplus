```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, a and b. words first convert both to numbers and then perform XOR
    """
    a = str(ord(a))
    b = str(ord(b))
    return chr(97+int((a^b)>>32))

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '12') == '123'
    assert string_xor('111', '1010') == '1101'
    assert string_xor('QSD', '192') == 'XIAP'

print("Testing finished")
```