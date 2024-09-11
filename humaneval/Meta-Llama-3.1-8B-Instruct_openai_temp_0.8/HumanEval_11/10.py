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
        str: XOR result as a binary string

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings")

    # Perform XOR operation on corresponding bits
    return ''.join('1' if (a_i == '1' and b_i == '0') or (a_i == '0' and b_i == '1') else '0' 
                    for a_i, b_i in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, checks if they are valid binary strings, and then performs binary XOR operation on corresponding bits. The function returns the result as a binary string.

The test cases at the end demonstrate the function's usage with different inputs.