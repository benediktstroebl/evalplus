```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): First input string.
        b (str): Second input string.
    
    Returns:
        str: Result of binary XOR operation as a string.
    
    Raises:
        ValueError: If input strings contain characters other than 1s and 0s.
    """
    
    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")
    
    # Use zip to iterate over characters of both strings in parallel
    # Use a generator expression to perform XOR operation on each pair of characters
    # Use join to concatenate the results into a single string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```