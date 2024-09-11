```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of XOR operation as a binary string.
    
    Raises:
        ValueError: If input strings are not of the same length or contain characters other than '0' or '1'.
    """
    
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Check if input strings contain only '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of '0' and '1'.")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on corresponding characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result
    
    # Return the final result string
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```