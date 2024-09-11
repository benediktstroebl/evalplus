```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Ensure input strings are of equal length
    assert len(a) == len(b), "Input strings must be of equal length"
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the input strings
    for i in range(len(a)):
        # Perform binary XOR operation on corresponding bits and append to result
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '010'))  # Expected output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes a test to ensure the input strings are of equal length and example use cases to demonstrate the function's behavior.