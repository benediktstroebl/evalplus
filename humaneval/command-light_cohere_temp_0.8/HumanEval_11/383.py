```python
import stringcase as sc
from typing import List


def string_xor(a: str, b: str) -> str:
    """ XOR two input strings a and b. import, 
    and return the result as a string.
    >>> sc.string_xor('010', '110')
    '100'
    """
    return sc.string_xor_string(sc.make_string_xor(a), b))


def string_xor_string(str1: str, str2: str) -> str:
    return str1 ^ str2


# Example usage:
input_str1 = '010'
input_str2 = '110'
result = string_xor_string(input_str1, input_str2)
print(result)  # Output: 100
``` 
This script defines a function `string_xor` that performs the XOR operation on two input strings and returns the result as a string. It also defines a function `string_xor_string` that implements the XOR operation by using the `^^` operator.  The result is a self-contained implementation of the XOR string function.