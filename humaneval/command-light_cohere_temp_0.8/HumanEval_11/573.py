```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings.
    :param
        string a a
    : string 
    :param string b: string 
    :return: string
    """
    return ''.join(c ^ int(b[i]) for i, c in enumerate(a) for b in b)

# Test
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('110', '010') == '001'
    assert string_xor('111', '1') == '11'
    assert string_xor('', '') == ''

# Test list of strings
def test_list_xor():
    assert list_string_xor(['010', '110', '111']) == ['100', '001', '11']

test_string_xor()
test_list_xor()
```