```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first input string.
        b (str): The second input string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Raises:
        ValueError: If either of the input strings contains characters other than 1 or 0.
    """
    
    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the result string
        result += xor_result
    
    # Return the result string
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

You can use this script as is, it includes example usage. The `string_xor` function takes two strings `a` and `b` as input, checks if they are valid (i.e., contain only 1s and 0s and are of the same length), performs the XOR operation on the corresponding characters, and returns the result as a string.