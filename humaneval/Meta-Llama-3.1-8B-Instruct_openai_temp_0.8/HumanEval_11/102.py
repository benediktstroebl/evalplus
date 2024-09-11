```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must be of the same length")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the input strings
    for i in range(len(a)):
        # Perform XOR operation on corresponding bits and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '011'))  # Output: '110'
```

This Python script defines a function `string_xor` that takes two binary strings as input and returns the result of their binary XOR operation. The function checks if both input strings are of the same length and performs the XOR operation bit by bit. The result is returned as a string. The script also includes some test cases to demonstrate the function's usage.