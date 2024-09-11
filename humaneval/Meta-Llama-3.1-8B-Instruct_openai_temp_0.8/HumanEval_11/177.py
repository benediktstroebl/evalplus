### Binary String XOR
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: Result of binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    if set(a).issubset('10') and set(b).issubset('10'):
        result = ''
        for i in range(max(len(a), len(b))):
            # Use XOR operator to compare bits at the same position
            # If bits are different, append 1 to result, else append 0
            result += str(int(a[i] == '0') ^ int(b[i] == '0'))
        return result
    else:
        raise ValueError("Input strings must consist only of 1s and 0s")


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '010'))  # Output: '111'
```
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR result as a string. The function first checks if the input strings are valid (i.e., consist only of 1s and 0s). If valid, it performs the XOR operation by comparing bits at the same position in both strings using the XOR operator. The result is then returned as a string. If the input strings are not valid, the function raises a `ValueError`.