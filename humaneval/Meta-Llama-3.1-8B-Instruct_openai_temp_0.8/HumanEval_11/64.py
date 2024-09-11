### Binary String XOR Operator
#### Problem Statement

Given two binary strings `a` and `b`, perform a binary XOR operation on them and return the result as a binary string.

#### Solution
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
    str: Binary string resulting from XOR operation.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Use the built-in zip and map functions to perform XOR operation
    # on corresponding bits of a and b, converting the result to int
    # and then to str to represent the binary result
    return ''.join(map(str, map(lambda x, y: int(x) ^ int(y), a, b)))

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```
This solution uses the built-in `zip` and `map` functions to iterate over the characters of `a` and `b` in parallel, performing the XOR operation on each pair of corresponding bits. The result is converted to a binary string using the `join` method and a generator expression.