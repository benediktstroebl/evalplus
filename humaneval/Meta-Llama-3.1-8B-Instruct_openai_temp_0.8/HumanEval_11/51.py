```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First string of 1s and 0s.
        b (str): Second string of 1s and 0s.

    Returns:
        str: Binary XOR result of a and b as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must be of the same length")

    # Use list comprehension to perform XOR operation on each character
    # and join the result into a string
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' 
                   for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '101'))  # Expected output: '000'
print(string_xor('111', '000'))  # Expected output: '111'
```

This script defines the `string_xor` function, which takes two binary strings as input, performs a bitwise XOR operation on each character, and returns the result as a string. The function includes input validation to ensure both strings are of the same length. The example use cases demonstrate the function's behavior with different input combinations.