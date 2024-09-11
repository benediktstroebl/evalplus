```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
        a (str): The first binary string consisting of 1s and 0s.
        b (str): The second binary string consisting of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs are binary strings
    if set(a).issubset('01') and set(b).issubset('01'):
        # Initialize an empty string to store the result
        result = ''
        
        # Iterate over the binary strings from left to right
        for i in range(max(len(a), len(b))):
            # Get the current bits from both strings, or 0 if out of range
            a_bit = int(a[i]) if i < len(a) else 0
            b_bit = int(b[i]) if i < len(b) else 0
            
            # Perform the XOR operation and convert the result to a string
            result += str(a_bit ^ b_bit)
        
        # Return the result
        return result
    else:
        # Raise an error if the inputs are not binary strings
        raise ValueError("Input strings must consist only of 1s and 0s")

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '111'))  # Output: '010'
print(string_xor('1111', '1111'))  # Output: '0000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs binary XOR operation on them, and returns the result as a binary string. It also includes input validation to ensure that the input strings consist only of 1s and 0s. The script includes example test cases at the end to demonstrate the function's usage.