```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR on the input strings.
    
    Raises:
    ValueError: If either input string contains characters other than 1 or 0.
    """

    # Check if input strings are valid (only contain 1s and 0s)
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings can only contain 1s and 0s")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Use zip() to iterate over characters in both strings in parallel
    # Use a generator expression to apply XOR to each pair of characters
    # Use join() to concatenate the results into a single string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```