```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Raises:
        ValueError: If the input strings are of different lengths.
        ValueError: If the input strings contain characters other than 1s and 0s.
    """
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use zip to pair up corresponding characters from a and b
    # Use a list comprehension to perform XOR on each pair
    # Convert the result back to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```