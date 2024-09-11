### Binary XOR String Function
#### A Python Script to Perform Binary XOR on Two Input Strings

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
        str: Binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))


# Example Usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Outputs: "100"
    print(string_xor('111', '000'))  # Outputs: "111"
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The example usage at the end demonstrates how to use the function with different inputs.