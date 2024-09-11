```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting of 1s and 0s.
    
    Parameters:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR operation on the input strings.
    """
    
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")
        
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of 1s and 0s.")
        
    # Initialize an empty result string
    result = ""
    
    # Perform XOR operation on each character in the strings
    for char_a, char_b in zip(a, b):
        # If the characters at the current position in both strings are different, append 1 to the result
        if char_a!= char_b:
            result += '1'
        # If the characters at the current position in both strings are the same, append 0 to the result
        else:
            result += '0'
    
    # If one string is a prefix of the other, append the remaining characters of the longer string to the result
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]
    
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings as input, performs binary XOR operation on them, and returns the result as a string. The function includes input validation to ensure that both inputs are strings consisting only of 1s and 0s. It uses the `zip` function to iterate over the characters in both strings in parallel and performs the XOR operation on each pair of characters. If one string is a prefix of the other, it appends the remaining characters of the longer string to the result. The example usage demonstrates the function's behavior with two sample input strings.