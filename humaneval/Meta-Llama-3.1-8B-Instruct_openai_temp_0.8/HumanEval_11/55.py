```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings (consisting only of 0s and 1s)")

    # Initialize an empty result string
    result = ''

    # Iterate over the input strings character by character
    for i in range(max(len(a), len(b))):
        # Get the characters at the current position, or '0' if out of bounds
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'

        # Perform the XOR operation and append the result to the output string
        result += str(int(bit_a) ^ int(bit_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '011'))  # Expected output: '110'
print(string_xor('111', '000'))  # Expected output: '111'
```

In this code:

- The `string_xor` function takes two binary strings `a` and `b` as input, checks if they are valid binary strings, and performs the binary XOR operation on them.
- It iterates over the characters of the input strings, performs the XOR operation on pairs of characters, and appends the result to the output string.
- The function includes a docstring that describes its purpose, parameters, and return value, as well as example use cases.
- The code includes test cases to verify the function's correctness.