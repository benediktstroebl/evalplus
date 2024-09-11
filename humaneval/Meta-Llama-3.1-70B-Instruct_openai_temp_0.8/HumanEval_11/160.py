```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are strings and have the same length
    if not (isinstance(a, str) and isinstance(b, str) and len(a) == len(b)):
        raise ValueError("Both inputs must be strings of the same length")
    
    # Check if strings consist only of 1s and 0s
    if not (set(a).issubset('10') and set(b).issubset('10')):
        raise ValueError("Strings must consist only of 1s and 0s")
    
    # Use zip to iterate over two strings simultaneously
    # Use a list comprehension to XOR each pair of bits
    # Use the int function with base 2 to convert binary strings to integers
    # Use the ^ operator to perform XOR operation
    # Use the format function to convert the result back to a binary string
    return ''.join(str(int(x)^int(y)) for x, y in zip(a, b))

# Example usage
print(string_xor('010', '110'))  # Outputs: 100
```