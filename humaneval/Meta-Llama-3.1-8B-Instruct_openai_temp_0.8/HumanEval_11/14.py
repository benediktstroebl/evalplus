```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use a list comprehension with the XOR operator (^) to perform the XOR operation
    result = ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '001'))  # Output: '100'
print(string_xor('1101', '1011'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. It also includes example usage and error checking to ensure the input strings are valid binary strings.