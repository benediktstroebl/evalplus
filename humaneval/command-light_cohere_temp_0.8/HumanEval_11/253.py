```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones.
    Return string a string a binary XOR on the first character of a and b,
    then carry the operation to the next character until one of them ends
    and returns the final result as a string.
    Args:
    a: first string to perform XOR operation on
    b: second string to perform XOR operation on
    Returns:
    str: result of XOR operation
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Input must be of type string")
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    result = []
    while a and b:
        if a[0] == b[0]:
            result.append(a[1])
            a = a[1:]
        else:
            result.append(b[1])
            b = b[1:]
    return ''.join(''.join(result)
```
This function performs the XOR operation on two input strings, which only contain the digit 1, and returns the result as a string.

Note that this code is self-contained and does not require any additional imports or external functions to solve the problem.