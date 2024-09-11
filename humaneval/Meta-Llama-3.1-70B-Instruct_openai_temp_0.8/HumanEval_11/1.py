```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation on the input strings as a string.
    
    Raises:
    ValueError: If the input strings are not of the same length or contain characters other than 1s and 0s.
    """
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Perform binary XOR operation on the input strings
    for i in range(len(a)):
        # XOR operation: 1 XOR 1 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, 0 XOR 0 = 0
        # We can use the!= operator to achieve the same result
        result += '1' if a[i]!= b[i] else '0'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```