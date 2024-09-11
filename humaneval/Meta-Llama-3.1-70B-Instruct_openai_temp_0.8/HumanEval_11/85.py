```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of 1s and 0s.")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result
    
    return result

# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```
This script defines a function `string_xor` that takes two strings of binary digits as input and returns their binary XOR as a string. It includes error checking to ensure that both strings have the same length and consist only of binary digits. The XOR operation is performed using the `^` operator, which is the bitwise XOR operator in Python. The result is returned as a string.