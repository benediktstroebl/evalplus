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
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use a list comprehension to perform XOR operation at the same time as the conversion to int
    # The XOR operation is done by converting each character to its corresponding integer and doing ^ operation.
    result = ''.join(str(int(i) ^ int(j)) for i, j in zip(a, b))

    # If the input strings are of different lengths, pad the shorter string with zeros
    result += '0' * (max(len(a), len(b)) - len(result))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes type hints and a docstring to describe the function's behavior and parameters. The function first checks if both inputs are binary strings (i.e., they consist only of 1s and 0s). If not, it raises a `ValueError`. Then it uses a list comprehension to perform the XOR operation by converting each character to its corresponding integer and doing a bitwise XOR operation. If the input strings are of different lengths, the function pads the shorter string with zeros. The function includes example use cases to demonstrate its behavior.