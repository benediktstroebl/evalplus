### Binary String XOR
#### Problem Statement
Input are two strings a and b consisting only of 1s and 0s. Perform binary XOR on these inputs and return result also as a string.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length")

    # Use a list comprehension to perform XOR on corresponding bits
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR on them, and returns the result as a string. It first checks if both inputs are of the same length, and if not, raises a ValueError. Then, it uses a list comprehension to perform XOR on corresponding bits of the two strings. Finally, it returns the result as a string. The example usage demonstrates how to use this function with different inputs.