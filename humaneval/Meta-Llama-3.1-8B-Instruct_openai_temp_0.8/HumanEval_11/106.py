```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR on two input strings consisting of 1s and 0s.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    # Use zip to iterate over characters in parallel, and '^' operator for XOR
    # The 'join' function is used to convert the result back into a string
    result = ''.join(str(int(c1) ^ int(c2)) for c1, c2 in zip(a, b))
    
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input, performs binary XOR on them, and returns the result as a string. It includes example usage at the end to demonstrate how to use the function.