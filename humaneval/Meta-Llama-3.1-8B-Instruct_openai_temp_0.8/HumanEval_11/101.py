### Binary String XOR
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use list comprehension and zip to iterate over characters from both strings
    # XOR operation: 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1, 0 ^ 0 = 0
    # Convert result list to string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('001', '110'))  # Output: '111'
```
This script defines a function `string_xor` that takes two binary strings as input, performs a bitwise XOR operation on them character-wise, and returns the result as a string. The `zip` function is used to iterate over characters from both strings simultaneously, and the list comprehension is used to apply the XOR operation. The result is then joined into a string using the `''.join()` method.