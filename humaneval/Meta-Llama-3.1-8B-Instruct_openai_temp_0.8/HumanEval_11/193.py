### Binary XOR of Two Strings
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings and returns the result as a string.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The binary XOR of the two input strings.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR by checking the bits and appending the result
        if char_a == '1' and char_b == '1':
            result += '0'
        elif char_a == '1' or char_b == '1':
            result += '1'
        else:
            result += '0'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1010'))  # Output: '0000'
```