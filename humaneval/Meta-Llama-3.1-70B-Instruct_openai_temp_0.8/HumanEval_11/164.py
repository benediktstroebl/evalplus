```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first string consisting only of 1s and 0s.
    b (str): The second string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Raises:
    ValueError: If either a or b contains characters other than 1 or 0.
    ValueError: If a and b are not of the same length.
    """
    
    # Check if a and b have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")
    
    # Check if a and b only contain 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Both strings must only contain 1s and 0s.")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in a and b
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
```