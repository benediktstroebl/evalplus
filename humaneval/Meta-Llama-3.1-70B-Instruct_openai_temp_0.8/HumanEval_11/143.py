```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Raises:
        ValueError: If either string contains characters other than '0' and '1'.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Check if both strings contain only '0' and '1'
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of '0' and '1'.")
    
    # Use the zip function to iterate over both strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of bits
    # Convert the result to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```