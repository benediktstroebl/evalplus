```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the current characters from the input strings, or the default value '0' if the index is out of range
        char_a = a[i] if i < len(a) else '0'
        char_b = b[i] if i < len(b) else '0'
        
        # Perform binary XOR on the current characters and append the result to the result string
        result += '1' if (char_a == '1' and char_b == '0') or (char_a == '0' and char_b == '1') else '0'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, performs binary XOR on them, and returns the result as a string. The function uses a simple iterative approach to perform the XOR operation on each pair of corresponding characters in the input strings. If one string is shorter than the other, the function pads the shorter string with zeros to match the length of the longer string. The function then returns the resulting string.