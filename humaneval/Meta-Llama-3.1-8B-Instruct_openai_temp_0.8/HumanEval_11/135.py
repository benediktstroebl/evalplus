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
        str: Binary string resulting from XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Input strings must consist only of 1s and 0s")

    return ''.join('1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(len(a)))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1010'))  # Output: '0000'
```