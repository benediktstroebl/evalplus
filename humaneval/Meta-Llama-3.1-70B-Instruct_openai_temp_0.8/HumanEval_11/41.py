```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): First string consisting of 1s and 0s.
    b (str): Second string consisting of 1s and 0s.
    
    Returns:
    str: Result of binary XOR operation as a string.
    """
    # Check if inputs are valid (consist only of 1s and 0s)
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length")

    # Perform XOR operation using zip and a list comprehension
    result = [str(int(x) ^ int(y)) for x, y in zip(a, b)]

    # Join the result list into a string
    return ''.join(result)


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings of binary digits as input, performs a binary XOR operation on them, and returns the result as a string. The function includes error checking to ensure the inputs are valid and of the same length. The example usage at the end demonstrates how to use the function.