```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Check if both characters are either '0' or '1'
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Both input strings must consist only of 1s and 0s")
        
        # Perform binary XOR on the characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, checks if they have the same length and consist only of '0's and '1's, and then performs a binary XOR operation on the corresponding characters of the input strings. The result is returned as a string.

You can run this script and use the `string_xor` function to perform binary XOR operations on binary strings.