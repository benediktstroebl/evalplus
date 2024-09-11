### Binary String XOR Operation
#### Script Description

This script defines a function `string_xor` that performs binary XOR operation on two input strings consisting only of 1s and 0s.

#### Script
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Resultant string after performing XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Use a list comprehension to XOR corresponding characters in the input strings
    result = ['1' if x!= y else '0' for x, y in zip(a, b)]
    
    # Join the result list into a string
    return ''.join(result)
```

#### Usage Example
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '101'))  # Output: '000'
```