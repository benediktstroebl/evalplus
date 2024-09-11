### Binary String XOR
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): First input string.
    b (str): Second input string.
    
    Returns:
    str: Result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Use a list comprehension to perform XOR operation on corresponding bits
    result = ''.join('1' if (int(a[i], 2) + int(b[i], 2)) % 2 else '0' for i in range(len(a)))
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1011', '1011'))  # Output: '0000'
```
This script uses a list comprehension to iterate over the input strings, perform the XOR operation by adding the corresponding bits and taking the result modulo 2, and join the results into a string. The `int(s, 2)` function is used to convert binary strings to integers.