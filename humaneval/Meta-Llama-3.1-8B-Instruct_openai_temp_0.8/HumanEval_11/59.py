```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    >>> string_xor('010', '110')
    '100'

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Result of XOR operation as string.
    """
    return ''.join('1' if (x == '1') ^ (y == '1') else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '010'))  # Expected output: '111'
```

In this script, we define a function `string_xor` that takes two binary strings `a` and `b` as input. It uses the `zip` function to iterate over the characters of `a` and `b` in parallel, performing a bitwise XOR operation on each pair of characters using the `^` operator. The result is a new binary string. The function is then tested with a few examples.