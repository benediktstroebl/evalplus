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
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip and a list comprehension to perform binary XOR operation on the input strings
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR result as a string. The function checks if the input strings consist only of 1s and 0s, and raises a `ValueError` if they do not. The XOR operation is performed using a list comprehension and the `zip` function, which pairs corresponding bits from the input strings. The result is joined into a single string using the `join` method.