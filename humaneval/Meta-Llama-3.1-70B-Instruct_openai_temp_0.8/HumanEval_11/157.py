```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of binary XOR operation on a and b as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result
    
    # Return the final result
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, checks if they are valid binary strings of the same length, performs binary XOR operation on them, and returns the result as a string. It also includes a test case to demonstrate the usage of the function.