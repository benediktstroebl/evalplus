```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
   
    a = a ^ b
    return ''.join_bytes(a ^ b)

def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("0011", "1010") == "0110"
    assert string_xor("001", "01") == "001"
    assert string_xor("000111", "01") == "111111"
    assert string_xor("1010", "10") == "01000"
    assert string_xor("0000", "1000") == "0000"

if __name__ == "__main__":
    test_string_xor()
```
This code provides a function that takes two strings consisting only of 0s and 1s, and performs a bitwise XOR operation on those strings, then returns the result as a string. The test_string_xor function contains various tests that check the correctness of the string_xor function with different input strings and expected output.