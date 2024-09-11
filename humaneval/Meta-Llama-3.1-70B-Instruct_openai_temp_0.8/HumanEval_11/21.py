```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The binary XOR result of a and b.
    """
    # Check if inputs are strings consisting only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be strings consisting only of 1s and 0s")
    
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length")
    
    # Perform XOR operation using zip and a list comprehension
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```