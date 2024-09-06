```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings a and b consisting only of single characters.
    :param[a] = '010'
    :param[b] = '110'
    :return: Returns '100'
    """
    a = set(a)
    b = set(b)
    result = ''.join(c ^ d for c, d in zip(a, b))
    return result
# Test case for the above function
string_xor('010', '110')
 ```
This function performs a XOR operation on two input strings, consisting only of single characters, and returns the result as a string. It uses the testing two input strings and performs the XOR operation, combining the corresponding characters in each string, and stores the result in the result variable.