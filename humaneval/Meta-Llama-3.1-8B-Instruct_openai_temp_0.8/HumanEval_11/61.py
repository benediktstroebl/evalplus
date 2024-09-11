```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): First binary string.
        b (str): Second binary string.
    
    Returns:
        str: Binary string resulting from XOR operation.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use list comprehension to XOR each character in the strings
    result = ''.join('1' if (a_char == '1' and b_char == '0') or (a_char == '0' and b_char == '1') else '0' 
                     for a_char, b_char in zip(a, b))
    
    # If one string is longer than the other, append the difference
    if len(a) > len(b):
        result += '0' * (len(a) - len(b))
    elif len(b) > len(a):
        result += '0' * (len(b) - len(a))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation to ensure that the input strings consist only of 1s and 0s, and it handles the case where one string is longer than the other by appending the difference as zeros. The function is tested at the end with an example usage.