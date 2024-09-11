```python
from typing import List, Tuple

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): First input string consisting of 1s and 0s.
    b (str): Second input string consisting of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")
    
    # Use map and lambda function to perform XOR operation on two strings
    result = ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '010'))  # Output: '111'
```