### Binary String XOR
#### Problem Statement and Solution

Given two binary strings `a` and `b`, we are asked to perform a binary XOR operation on them and return the result as a string.

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input binary strings.

    Args:
    a (str): A binary string consisting only of '0's and '1's.
    b (str): A binary string consisting only of '0's and '1's.

    Returns:
    str: The result of the binary XOR operation as a binary string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the input strings character by character
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result to the string
        result += str(int(char_a) ^ int(char_b))

    # If the input strings have different lengths, append the remaining characters of the longer string to the result
    result += a[len(b):] if len(a) > len(b) else b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a binary string. The function iterates over the input strings character by character, performs the XOR operation, and appends the result to the output string. If the input strings have different lengths, the function appends the remaining characters of the longer string to the result. The script also includes test cases to demonstrate the function's correctness.