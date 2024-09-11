```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two binary strings.
    
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
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the current characters
        # The XOR operation is performed using the!= operator, which returns True if the characters are different
        # The result is converted to an integer (1 or 0) using the int() function
        # The result is converted back to a string using the str() function
        result += str(int(char_a!= char_b))
    
    # Return the result string
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function includes error checking to ensure that the input strings have the same length and consist only of 1s and 0s. The XOR operation is performed using the!= operator, which returns True if the characters are different. The result is converted to an integer (1 or 0) using the int() function and then converted back to a string using the str() function.