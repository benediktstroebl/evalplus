```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two input strings a and b.
    The input strings should consist only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of the XOR operation as a binary string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result
    
    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```