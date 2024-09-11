```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting of 1s and 0s.
    
    Parameters:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform XOR operation and convert the result to a binary string
        result += str(int(i) ^ int(j))
    
    # Return the result
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

In this script, the `string_xor` function performs binary XOR operation on two input strings `a` and `b`. It checks if the inputs are valid binary strings, then iterates over the characters in the input strings, performs XOR operation on each pair of characters, and finally returns the result as a string. The script also includes a test case to demonstrate the function's usage.