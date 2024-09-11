```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform binary XOR on the current characters and append the result
        result += str(int(a[i]) ^ int(b[i]))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result as a string. It first checks if the input strings are of the same length, then iterates over the characters in the input strings, performs binary XOR on each pair of characters, and appends the result to the output string. Finally, it includes some test cases to demonstrate the function's usage.