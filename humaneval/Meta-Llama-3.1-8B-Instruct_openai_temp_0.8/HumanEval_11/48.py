```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    The input strings are expected to consist only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The binary string result of the XOR operation.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if c1!= c2 else '0' for c1, c2 in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their XOR result as a string. It uses a generator expression inside the `join` function to iterate over the characters of the input strings and apply the XOR operation. If the characters at the same position in the two strings are different, the result is '1'; otherwise, it's '0'. The `zip` function is used to iterate over the characters of the two strings in parallel.