```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting of 1s and 0s.
    
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
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty list to store the XOR result
    result = []
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR on the current characters and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))
    
    # Join the result list into a string and return it
    return ''.join(result)

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```