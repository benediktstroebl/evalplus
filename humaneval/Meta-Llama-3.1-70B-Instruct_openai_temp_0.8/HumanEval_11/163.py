```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first string consisting only of 1s and 0s.
    b (str): The second string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation on the input strings.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the strings
    for char_a, char_b in zip(a, b):
        # Check if characters are either '0' or '1'
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Both strings must consist only of 1s and 0s.")
        
        # Perform XOR operation
        if char_a == char_b:
            result += '0'
        else:
            result += '1'
    
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```