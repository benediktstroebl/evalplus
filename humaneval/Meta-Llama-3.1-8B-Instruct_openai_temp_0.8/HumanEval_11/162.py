```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation as a string.
    """
    
    # Ensure both inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")
    
    # Use a list comprehension to perform XOR operation bit by bit
    result = ''.join('1' if a[i]!= b[i] else '0' for i in range(len(a)))
    
    return result

# Test cases
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '101'))  # Expected output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input and returns the result of their XOR operation. It first checks if the input strings are of equal length, then uses a list comprehension to perform the XOR operation bit by bit, and finally returns the result as a string. The script also includes some test cases to demonstrate the function's usage.