```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings and return the result.

    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.

    Returns:
        str: The result of the XOR operation as a binary string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Strings must be of the same length")

    result = ''
    for i in range(len(a)):
        # XOR the corresponding bits and append the result to the string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
```

This script defines the `string_xor` function, which takes two binary strings as input and returns their binary XOR result. It checks if the input strings are of the same length, and if not, raises a `ValueError`. The function then iterates over the characters in the input strings, performs a binary XOR operation on each pair of bits, and appends the result to the output string. Finally, it returns the resulting binary string.