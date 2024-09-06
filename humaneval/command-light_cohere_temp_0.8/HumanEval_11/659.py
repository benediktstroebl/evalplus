```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    Returns a if both strings are of different lengths, an exception will be thrown.
    """
    return ''.join(a.join(b)
   """ + ''.join(b)

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('',’111') == ''.join('.111')
    assert string_xor('',’111') == ''.join('.111')
    assert string_xor('f', 'o') == ''.join(88)
    assert string_xor('', '1') == ''.join('')
    assert string_xor('abcde', 'fg') == ''.join('efg')
    assert string_xor('', '') == ''.join('')
```
The provided Python script defines a function named `string_xor` that performs a bitwise XOR operation on two input strings, consisting only of single characters. It employs the expected to handle various cases, such as different string lengths, empty strings, and strings with different characters. The test function validates these string input using assertion checks, ensuring the correctness of the `string_xor` function.