```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings a and b consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s.")
    
    # Use zip to iterate over both strings simultaneously
    # Use a list comprehension to perform XOR on each pair of characters
    # Convert the result to a string using join
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```