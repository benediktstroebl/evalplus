```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of '0's and '1's
    Perform binary XOR on the inputs and return the result.
    return aa operation on the two elements.
    return a strings.
    """ a integer bit a in the string is a list of integers from 0 to 9.
    """
```
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("aa", "bb") == "aa"
    assert string_xor("", "") == ""
    assert string_xor("1234567890") == "0"
    assert string_xor("12345678", "9") == "78"
    assert string_xor("QWERTZtasdf", " 1234 ) ]") == "QWERTZtasdf"
    assert string_xor("abc", "123") == "abc"

test_string_xor()
```