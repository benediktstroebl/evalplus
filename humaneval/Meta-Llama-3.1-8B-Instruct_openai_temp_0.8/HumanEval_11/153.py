### Binary XOR on Strings of 1s and 0s
### ================================
### A Python function to perform binary XOR on two input strings.

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The binary XOR of a and b as a string.
    
    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters and convert to string
        result += str(int(char_a) ^ int(char_b))
    
    # If one of the input strings is shorter than the other, 
    # append the remaining characters from the longer string
    result += ''.join(str(int(char)) ^ 0 for char in a[len(b):] if len(b) < len(a))
    result += ''.join(str(int(char)) ^ 0 for char in b[len(a):] if len(a) < len(b))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
print(string_xor('1111', '0000'))  # Output: '1111'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on each pair of characters, and returns the resulting binary string. It handles cases where the input strings have different lengths by appending the remaining characters from the longer string. The script also includes example use cases to demonstrate the function's behavior.