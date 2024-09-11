```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Raises:
    ValueError: If the input strings are not of the same length.
    ValueError: If the input strings contain characters other than '0' and '1'.
    """
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Check if the input strings contain only '0' and '1'
    for char in a + b:
        if char not in ['0', '1']:
            raise ValueError("Input strings must consist only of '0' and '1'.")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR on the current characters and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```