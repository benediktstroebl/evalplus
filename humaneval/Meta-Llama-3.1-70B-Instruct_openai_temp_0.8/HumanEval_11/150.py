```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): First input string.
        b (str): Second input string.
    
    Returns:
        str: Result of XOR operation as a string.
    
    Raises:
        ValueError: If input strings are not of the same length or contain characters other than 1 and 0.
    """
    # Check if inputs are valid
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Perform XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```