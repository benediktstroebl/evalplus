```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    The input strings should consist only of 1s and 0s.
    
    Args:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR operation as a string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings should have the same length.")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings should consist only of 1s and 0s.")
    
    # Use zip to iterate over the characters in both strings in parallel
    # Use a list comprehension to perform XOR operation on each pair of characters
    # Convert the result to a string
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```