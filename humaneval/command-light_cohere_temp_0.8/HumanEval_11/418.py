```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ 
    Function performs binary XOR on two input strings a and b 
    and returns the result as a string.

    : Input strings a string 
    are only consisting of 1s and 0s.
    """
    result = ''.join([ord(c) == ord('0') for c in a] ^ [ord(c) == ord('0') for c in b])
    return ''.join(result)

# Test cases 

def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '10') == '0110'
    assert string_xor('000', '00') == '0000'
    assert string_xor('111', '1') == '1111'

# main function 
test_xor()
```

The code defines a function `string_xor` that takes two strings a and b, consisting only of ones and zeros, and performs the binary XOR operation on them. The `test_xor` function contains a series of test cases that verify the functionality of the `string_xor` function with various input strings. 
In summary, the code provides a self-contained solution and test suite for the given problem.