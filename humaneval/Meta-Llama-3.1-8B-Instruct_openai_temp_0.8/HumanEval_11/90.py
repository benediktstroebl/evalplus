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
    """
    # Check if both inputs are binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the inputs and apply XOR operation
    for xa, xb in zip(a, b):
        result += str(int(xa) ^ int(xb))

    return result


# Test the function with example inputs
print(string_xor('010', '110'))  # Expected output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a binary string. It includes a check to ensure that the inputs are binary strings, consisting only of 1s and 0s. The script also includes a test case to demonstrate the function's behavior.