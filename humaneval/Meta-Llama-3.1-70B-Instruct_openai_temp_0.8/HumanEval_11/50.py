```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    Both a and b should consist only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of binary XOR operation on a and b.
    """
    
    # Check if inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")
        
    # Check if inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must consist only of 1s and 0s.")
        
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")
        
    # Perform binary XOR operation
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```