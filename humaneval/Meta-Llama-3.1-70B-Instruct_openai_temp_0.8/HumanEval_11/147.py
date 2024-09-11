```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two input strings.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform the XOR operation on the current characters
        # The XOR operation is equivalent to checking if the characters are different
        xor_result = '1' if a[i]!= b[i] else '0'
        
        # Append the result to the result string
        result += xor_result
    
    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```