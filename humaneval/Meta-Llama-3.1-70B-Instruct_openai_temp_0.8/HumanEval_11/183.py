```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if the lengths of the input strings are equal
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use the zip function to iterate over the characters in the input strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # Use the join function to concatenate the results into a single string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```