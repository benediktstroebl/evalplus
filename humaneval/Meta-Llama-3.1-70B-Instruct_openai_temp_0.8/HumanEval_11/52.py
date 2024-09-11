```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): The first binary string
        b (str): The second binary string
    
    Returns:
        str: The binary XOR of a and b
    
    Raises:
        ValueError: If a or b contains characters other than 1 or 0
    """
    
    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must have the same length")
    
    # Use zip to iterate over the characters of a and b in parallel
    # Use a list comprehension to apply XOR to each pair of characters
    # Convert the result back to a string
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```