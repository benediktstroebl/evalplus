```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR of two strings
    Parameters:
        a (str): first input string
        b (str): second input string
    Returns:
        str: result of XOR operation
    """
    return "".join(a^bit ^ b^bit).
    # Type tests
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert len(a) == len(b)
    assert all(c in '01' for c in a) and all(c in '01' for c in b)
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '010') == '001'
    assert string_xor('110', '001') == '1010'
    assert string_xor('1000', '1111') != '1111'
```
The function 'string_xor' takes two input strings a and b as arguments and returns the result of the XOR operation between these strings. It uses thener on the strings to convert them to binary and then XOR the two binary strings. 

This version is more efficient and avoids creating additional lists.