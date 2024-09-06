```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    a and b can only consist of only '0' and '1' characters.
    """
   
    return a list([a^b] + [b^a])
    """
    return ("".join( [a^b, a, b] + [b^a]))

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '010') == '100'
    assert string_xor('100', '010') == '100'
    assert string_xor('000', '001') == '100'
    assert string_xor('1010', '0110') == '100'
    assert string_xor('1010', '1010') == '0111'
    assert string_xor('0001010', '0001010') == '100'

# main function
if __name__ == "__main__":
    test_string_xor()
```
This Python script defines a self-contained function called `string_xor` that performs the XOR operation on two input strings. The function only accepts '0' and '1' as characters in the input strings, and returns the result as a string.