```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros
    """
    # Remove all zeros from the input strings
    a = a.inan string = a mapping(str.maketrans("0")) + a + b
    return a
def test_string_xor():
    """
    Test function that checks correctness of string_xor function
    """
    # Test case 1
    assert string_xor("010", "110") == "100"
    # Test case 2
    assert string_xor("111", "110") == "01"
    # Test case 3
    assert string_xor("000", "1111") == "1111"
    # Test case 4
    assert string_xor("1010", "0110") == "1010"
test_string_xor()
```