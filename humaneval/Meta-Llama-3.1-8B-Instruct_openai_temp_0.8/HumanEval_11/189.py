### Binary String XOR
#### Problem Description
Perform binary XOR on two input strings consisting only of '0' and '1'.

#### Solution
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

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length")

    # Initialize result string
    result = ""

    # Iterate through each character in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on current characters and append result
        result += str(int(char_a) ^ int(char_b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```
This script performs binary string XOR by iterating through each character in the input strings, performing the XOR operation on the corresponding characters, and appending the result to the output string. It also includes input validation to ensure the input strings are of the same length.