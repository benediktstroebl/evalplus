### Binary String XOR
#### Problem Description
Perform binary XOR operation on two binary strings.

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
        str: Result of binary XOR operation on 'a' and 'b'.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return str(int(a, 2) ^ int(b, 2))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This Python script uses the built-in `int` function to convert binary strings to integers, performs the XOR operation using the `^` operator, and then converts the result back to a string using `str`. The `int` function is called with base 2 to denote binary conversion.