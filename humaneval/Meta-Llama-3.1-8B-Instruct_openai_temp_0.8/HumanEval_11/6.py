### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two binary strings and return the result as a string.

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
        str: Binary XOR result of a and b as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs are binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings")

    # Use list comprehension to apply XOR operation element-wise
    result = ['1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0'
              for x, y in zip(a, b)]
    
    # Join the result list into a string
    return ''.join(result)
```

#### Example Use Cases

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('111', '000'))  # Output: '111'
```