```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first input string consisting of 1s and 0s.
    b (str): The second input string consisting of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Raises:
    ValueError: If the input strings are of different lengths or contain characters other than 1s and 0s.
    """
    
    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```