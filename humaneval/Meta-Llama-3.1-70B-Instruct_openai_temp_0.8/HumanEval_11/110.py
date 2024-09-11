```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR on two input strings a and b.
    
    Parameters:
    a (str): A string consisting only of 1s and 0s.
    b (str): A string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation on a and b as a string.
    """
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```