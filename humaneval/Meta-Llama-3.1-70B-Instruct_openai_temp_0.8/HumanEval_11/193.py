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
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    # Return the result string
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR as a string. The function includes error checking to ensure that the input strings have the same length and consist only of 1s and 0s. The example usage at the end demonstrates how to use the function.