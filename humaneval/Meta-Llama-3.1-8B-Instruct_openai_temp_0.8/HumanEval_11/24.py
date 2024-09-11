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
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s.")

    # Use list comprehension and zip to perform XOR operation
    # If a[i] == '1' and b[i] == '1' or vice versa, result[i] will be '0'
    # Otherwise, result[i] will be '1'
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    # If one string is shorter than the other, fill the result with the corresponding bit
    result += a[-1] * (len(b) - len(a)) + b[-1] * (len(a) - len(b))

    return result
```

This script performs a binary XOR operation on two strings consisting only of 1s and 0s, and returns the result as a string. If the strings have different lengths, the script fills the result with the corresponding bit (0 or 1) from the end of the longer string. The function handles exceptions for invalid inputs.