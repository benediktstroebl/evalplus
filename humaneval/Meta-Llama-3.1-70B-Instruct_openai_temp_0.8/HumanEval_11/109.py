```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): The first input string consisting of 1s and 0s.
    b (str): The second input string consisting of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation on input strings as a string.
    """
    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use zip to iterate over two strings in parallel
    # Use a list comprehension to perform XOR operation on corresponding characters
    # Convert the result back to a string using join
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Outputs: 100
```