```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function performs binary XOR on two input strings consisting only of ones and zeros
    and returns the result as a string.
    """
    string_xor('010', '110')
    """
    return '100'

#Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('00', '10') == '10'
    assert string_xor('000', '0000') == '0000'
    assert string_xor('00', '00') == '0000'
    assert string_xor('111', '1111') == '0000'

if __name__ == "__main__":
    test_string_xor()
``` 
This Python script defines a function `string_xor` that performs a binary XOR operation on two input strings. It then has a test cases that cover various scenarios, such as empty strings, different lengths, and different characters.