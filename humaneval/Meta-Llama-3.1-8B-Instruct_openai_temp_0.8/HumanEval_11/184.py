### Binary String XOR
### ===============

Below is a Python function that performs binary XOR operation on two input strings.

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary string result of XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if both strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")

    # Initialize empty result string
    result = ""

    # Iterate over each character in the strings
    for i in range(len(a)):
        # Perform XOR operation and convert result to string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '111'))  # Output: '000'
```

This function works by iterating over each character in both input strings, performing a binary XOR operation, and appending the result to a new string. The result is returned as a string of binary digits ('0's and '1's).