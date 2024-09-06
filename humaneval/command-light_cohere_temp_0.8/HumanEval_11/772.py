```python
import stringcase as tc
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    >>> result = tc.string_xor('010', '110')
    assert result == '100'
    """
    return tc.string('01', '10')
```
The code defines a function named `string_xor` that performs the XOR operation on two input strings, which must contain only the characters '01' and '10'. The function returns the result of the XOR operation as a string.

It then passes the function with two test strings and asserts that the result is equal to the expected output '100'.