```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first string consisting of 1s and 0s.
    b (str): The second string consisting of 1s and 0s.
    
    Returns:
    str: The binary XOR result as a string.
    """
    
    # Ensure both strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR operation on each pair of characters
        # Convert characters to integers (0 or 1), perform XOR, and convert back to string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'

# Test cases:
print(string_xor('0', '0'))   # Output: '0'
print(string_xor('1', '1'))   # Output: '0'
print(string_xor('0', '1'))   # Output: '1'
print(string_xor('1', '0'))   # Output: '1'
```