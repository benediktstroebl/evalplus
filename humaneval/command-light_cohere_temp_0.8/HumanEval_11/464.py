```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b consisting only of 1s and 0s.
    """
    return ''.join([(x == '1') for x in a] ^ [x == '1' for x in b])

# Tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('11', '11') == '000'
    assert string_xor('111', '01') == '100'
test_string_xor() 
```
This code defines a function called `string_xor`, which performs the XOR operation on two input strings. It uses the neither `type` nor `List` annotations, and the function returns the result as a string. 

The test function verifies the correctness of the `string_xor` function with the provided test cases.