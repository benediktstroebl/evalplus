```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): First input string.
    b (str): Second input string.
    
    Returns:
    str: Result of binary XOR operation.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform XOR operation and append the result to the list
        result.append(str(int(i) ^ int(j)))
    
    # Join the result list into a string and return it
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that performs binary XOR operation on two input strings consisting only of 1s and 0s. It checks if both inputs are valid, performs the XOR operation, and returns the result as a string. The script also includes example use cases and error handling.