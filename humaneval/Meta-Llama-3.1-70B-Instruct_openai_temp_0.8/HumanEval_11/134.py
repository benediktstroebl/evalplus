```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings a and b.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must have the same length")
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))
    
    # Join the characters in the list into a string and return the result
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```