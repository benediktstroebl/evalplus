```markdown
### Binary String XOR
#### Problem Statement
Given two binary strings `a` and `b` consisting only of 1s and 0s, perform binary XOR operation on them and return the result as a string.

#### Solution
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Parameters:
    a (str): First binary string
    b (str): Second binary string

    Returns:
    str: Binary string result of XOR operation

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Perform XOR operation on integers
    result = int_a ^ int_b

    # Convert result back to binary string and remove '0b' prefix
    result_str = bin(result)[2:]

    return result_str

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '001'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input, performs XOR operation on them, and returns the result as a binary string. The example usage at the end demonstrates how to use this function with different inputs.