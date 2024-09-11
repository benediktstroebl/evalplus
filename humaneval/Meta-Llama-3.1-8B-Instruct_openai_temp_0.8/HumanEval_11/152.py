### Binary XOR Operation on Strings
###======================================
### 
### This script performs binary XOR operation on two binary strings.

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
    # Use the zip function to iterate over both strings simultaneously
    # The XOR operation is performed using the '^' operator
    # The result is converted back to a string
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input. It uses the `zip` function to iterate over both strings simultaneously, performing the XOR operation using the `^` operator. The result is converted back to a string using the `join` method. The function includes docstrings with examples to demonstrate its usage.