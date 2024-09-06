```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    """ a return the XOR the string in a specific format.
    >>> string_xor('010', '110')
    '100'
    """
    return ("".join(c ^ d) for c, d in zip([x for x in a], [y for y in b]))

# Test
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("111", "000") == "111"
    assert string_xor("111", "1111") == "1111"
    assert string_xor("000", "0") == "0"
    assert string_xor("111", "110") == "1110"
    assert string_xor("00", "00") == "0000"
    assert string_xor("1111", "1111") == "11111111"

# Usage
if __name__ == "__main__":
    test_string_xor()
```