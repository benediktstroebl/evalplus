```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two input strings a and b.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform the XOR operation on the corresponding characters
        # The XOR operation in Python can be performed using the!= operator for boolean values
        # The int function is used to convert the characters to integers (0 or 1)
        # The str function is used to convert the result back to a string
        result += str(int(a[i])!= int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```