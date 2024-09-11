```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    
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
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform binary XOR operation on the corresponding characters
        # and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```