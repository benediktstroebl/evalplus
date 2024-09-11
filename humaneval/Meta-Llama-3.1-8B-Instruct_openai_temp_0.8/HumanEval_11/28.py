```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first string consisting of 1s and 0s.
    b (str): The second string consisting of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the corresponding characters from the input strings
        # If a character is out of range, use '0' as a default value
        char_a = a[i] if i < len(a) else '0'
        char_b = b[i] if i < len(b) else '0'
        
        # Perform binary XOR operation and convert to string
        # '1' if the sum is odd, '0' if the sum is even
        result += str((int(char_a) + int(char_b)) % 2)
    
    # Return the result
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, performs binary XOR operation, and returns the result as a string. The function iterates over the characters in the input strings, performs binary XOR operation, and converts the result to a string. The test case at the end demonstrates how to use the function.