```markdown
# Binary String XOR
=====================

This script performs binary XOR operation on two input strings.

### Code

```python
from typing import Iterable

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
        a (str): First input string.
        b (str): Second input string.
    
    Returns:
        str: Result of XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are strings consisting of only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist of only 1s and 0s")

    # Use zip to iterate over characters of both strings in parallel
    # Use a list comprehension to apply XOR operation on each pair of characters
    # Convert the result to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
```

### Example Use Case

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```
```