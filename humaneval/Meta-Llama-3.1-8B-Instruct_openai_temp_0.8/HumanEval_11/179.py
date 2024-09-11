### Binary String XOR
#### Problem Statement

Perform binary XOR on two input strings consisting only of 1s and 0s.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Use list comprehension to perform XOR operation on corresponding bits
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs the XOR operation on corresponding bits, and returns the result as a string. The function uses list comprehension and the `zip` function to iterate over the input strings. The `join` method is used to concatenate the results into a single string. The script also includes example use cases to demonstrate the function's behavior.