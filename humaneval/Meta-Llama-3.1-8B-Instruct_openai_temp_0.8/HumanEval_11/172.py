```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
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
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings.")

    # Initialize an empty result string
    result = ''

    # Iterate through the inputs and perform binary XOR
    for i, j in zip(a, b):
        result += str(int(i) ^ int(j))

    # If inputs have different lengths, fill the result with the remaining input
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script includes the `string_xor` function and some test cases. The function takes two binary strings as input and returns the result of the binary XOR operation. It also includes error checking to make sure the inputs are valid binary strings.