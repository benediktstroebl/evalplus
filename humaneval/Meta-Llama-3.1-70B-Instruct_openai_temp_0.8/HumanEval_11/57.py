```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR operation as a string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR operation on the corresponding characters
        # Convert the characters to integers (0 or 1), perform XOR, and convert back to string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```