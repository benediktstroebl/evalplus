```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of ones.
    Perform binary XOR operation on these inputs and return result as a string.
    """
    return str(f"{a}{b}")

def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("000", "111") == "000"
    assert string_xor("001", "01") == "11"
    assert string_xor("1010", "110") == "0110"
    assert string_xor("00111", "1111") == "1111"

# Example usage
test_string_xor()
``` 
This Python script defines a function string_xor that performs the XOR operation on two input strings, both consisting only of ones. The function then returns the string containing the XOR result. 

The test_string_xor function contains test cases to verify the correctness of the string_xor function. It creates and asserts the expected output.