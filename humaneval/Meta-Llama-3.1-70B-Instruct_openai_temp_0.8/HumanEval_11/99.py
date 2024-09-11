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
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Perform binary XOR operation
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes error checking to ensure that the input strings have the same length and consist only of 1s and 0s. The XOR operation is performed using a generator expression within the `join` function. The example usage demonstrates the function's behavior with the provided test case.