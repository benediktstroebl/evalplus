```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): A string consisting of only 1s and 0s.
    b (str): A string consisting of only 1s and 0s.
    
    Returns:
    str: The result of the XOR operation as a string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Perform XOR operation on the input strings
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```