### Binary String XOR
#### Problem Description

This Python script performs binary XOR operation on two input strings consisting of 1s and 0s.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use map function to iterate over corresponding characters in both strings
    # and xor them together using the int function to convert them to integers
    # and the ^ operator for the XOR operation
    # Finally, use the str function to convert the result back to a string
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script first checks if both input strings are valid binary strings. If not, it raises a ValueError. Then it uses the map function and a generator expression to iterate over corresponding characters in both strings, perform the XOR operation, and return the result as a string.