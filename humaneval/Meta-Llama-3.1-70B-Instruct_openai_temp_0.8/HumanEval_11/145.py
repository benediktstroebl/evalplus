```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first string.
        b (str): The second string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    """
    
    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # XOR of '0' and '0' is '0', XOR of '1' and '1' is '0', XOR of '0' and '1' is '1', XOR of '1' and '0' is '1'
        # So, we can simply return a character that is different from both char_a and char_b if they are the same
        # Otherwise, return the same character as char_a (or char_b)
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the XOR result to the result string
        result += xor_result
    
    # Return the result string
    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```