```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): The first input string consisting of 1s and 0s.
    b (str): The second input string consisting of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Ensure both inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Both input strings must be of equal length.")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over both input strings using zip
    for bit_a, bit_b in zip(a, b):
        # Perform binary XOR operation and append the result to the result string
        result += str(int(bit_a) ^ int(bit_b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes example usage and error handling to ensure both input strings are of equal length.