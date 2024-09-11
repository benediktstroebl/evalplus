```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
    >>> string_xor('010', '110')
    '100'

    :param a: Binary string (only 1s and 0s)
    :param b: Binary string (only 1s and 0s)
    :return: Binary string (only 1s and 0s) after XOR operation
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    result = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        else:
            result += '1'

    return result


# Example usage:
print(string_xor('010', '110'))
print(string_xor('111', '000'))
print(string_xor('101', '101'))
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a binary string. It checks if the input strings are of the same length and raises a `ValueError` if they are not. The function then iterates over each bit position in the input strings, applies the XOR operation, and constructs the result string. The example usage at the end demonstrates how to use the function with different input strings.