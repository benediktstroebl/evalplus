```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string
        b (str): Second binary string

    Returns:
        str: Binary string result of XOR operation

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only consist of 1s and 0s")

    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a bitwise XOR operation on each pair of corresponding bits, and returns the result as a binary string. It also includes some example usage of the function and checks to ensure the input strings only consist of '1' and '0' characters.