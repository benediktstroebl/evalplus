```python
import stringio
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, using only characters from numbers 0-
    1.
    Return the string
    result
    """
    xor = ""
    while a or b:
        xor = chr(97 + (ord(a) ^ ord(b)))
        a, b = a[0], b[0]
    return xor
def test_xor():
    test_list = [
        "010".join, 
        "110".join(), 
        "00110".join(), 
        "011010".join(),
        "1010".upper(),
        "001010".upper()
    ]
    for test_case in test_list:
        got = string_xor(test_case[0], test_case[1])
        assert got == test_case[2]
if __name__ == "__main__":
    test_xor()
    print("All tests passed!")
```