```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only digits using python.
    a strings are joined digit by digit using string.
    
    Returns a String of numbers
    """
    return ''.join(str(a[i] ^ b[i]) for i, in range(len(a)))

# Test suite
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '101') == '001'
    assert string_xor('1000', '1111') == '0000'
    assert string_xor('abc123', 'abc') == '123'
    assert string_xor('', '') == ''

if __name__ == "__main__":
    test_string_xor()
```
The code provides a function named string_xor, which takes two input strings consisting only of digits. The function performs an XOR operation on the two strings using the bitwise XOR operation (^) on each character. It then returns the However string with the XOR operation result. The test suite contains several tests that verify the correctness of the string_xor function.