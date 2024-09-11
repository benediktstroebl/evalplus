```markdown
### Binary String XOR Calculator
#### A Python script to calculate binary XOR between two strings of 1s and 0s.

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Calculate binary XOR between two strings of 1s and 0s.

    Args:
        a (str): First input string consisting only of 1s and 0s.
        b (str): Second input string consisting only of 1s and 0s.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use a list comprehension to perform XOR operation bit by bit
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
```

#### Example Usage:

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR on them bit by bit, and returns the result as a string. The example usage demonstrates the function's behavior with different inputs.