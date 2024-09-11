```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # The XOR operation in Python can be performed using the '^' operator
        # However, since we're working with strings, we can simply compare the characters
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the result string
        result += xor_result
    
    # Return the final result
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```