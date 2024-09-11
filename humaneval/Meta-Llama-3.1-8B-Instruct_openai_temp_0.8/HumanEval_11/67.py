### Binary String XOR
#### A Python Script to Perform Binary String XOR

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A binary string.
    b (str): A binary string.

    Returns:
    str: The binary string result of XOR operation.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Inputs must be strings.")

    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s.")

    # Use list comprehension to apply XOR operation on corresponding bits
    result = ['1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0'
              for bit_a, bit_b in zip(a, b)]

    # Join the result list into a string
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '110'))  # Expected output: '011'
print(string_xor('111', '111'))  # Expected output: '000'
```

This script defines the `string_xor` function to perform binary XOR operation on two input strings. It includes input validation and error handling to ensure the inputs are strings consisting only of 1s and 0s. The function returns the result as a string. The test cases demonstrate the function's behavior with different inputs.