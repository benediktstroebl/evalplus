```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The binary XOR result as a string.
    """
    
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings consisting only of 1s and 0s.")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must have the same length.")
    
    # Perform binary XOR using zip and a list comprehension
    xor_result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return xor_result


# Test the function
print(string_xor('010', '110'))  # '100'
```