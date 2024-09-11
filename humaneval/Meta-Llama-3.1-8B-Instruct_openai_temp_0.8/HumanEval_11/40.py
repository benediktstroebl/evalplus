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
        str: Result of XOR operation on a and b

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current bits
        result_bit = str(int(char_a) ^ int(char_b))
        # Append the result bit to the result string
        result += result_bit

    # If the input strings are of different lengths, append the remaining bits from the longer string
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. The function uses a simple iterative approach to calculate the XOR of corresponding bits in the input strings. It also handles the case where the input strings are of different lengths by appending the remaining bits from the longer string. The script includes a docstring that provides a detailed explanation of the function's behavior, including its parameters, return value, and examples of use.