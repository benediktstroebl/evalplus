```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two input strings.
    
    Args:
        a (str): The first input string, consisting only of 1s and 0s.
        b (str): The second input string, consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation, returned as a string.
    """
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR operation on the current characters and append to the result
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```