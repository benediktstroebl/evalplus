```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.

    Returns:
        str: The result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the current bits from the input strings
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'

        # Perform XOR operation and append the result to the output string
        result += str(int(bit_a) ^ int(bit_b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. The function uses a simple iterative approach to perform the XOR operation bit-by-bit, and handles cases where the input strings are of different lengths.