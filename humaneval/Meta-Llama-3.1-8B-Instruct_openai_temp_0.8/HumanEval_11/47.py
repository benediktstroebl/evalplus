### Binary XOR String Operation
#### Python Script
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
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform XOR operation on the current characters and append to result
        result += str(int(i) ^ int(j))

    # If the input strings are of different lengths, append the remaining characters
    result += a[len(b):] if len(a) > len(b) else b[len(a):]

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1011'))  # Output: '0001'
print(string_xor('101', '101'))  # Output: '000'
```