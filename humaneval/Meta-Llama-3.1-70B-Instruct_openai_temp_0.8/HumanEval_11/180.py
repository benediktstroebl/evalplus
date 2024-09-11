```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Perform binary XOR operation
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, checks their validity and length, and returns the result of the binary XOR operation as a string. The XOR operation is performed using a generator expression that iterates over the input strings in parallel using the `zip` function, converts each character to an integer, performs the XOR operation, and converts the result back to a string.