```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings.
    
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
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for bit_a, bit_b in zip(a, b):
        # Perform XOR operation on the current bits and append the result to the result string
        result += str(int(bit_a) ^ int(bit_b))
    
    return result


# Test cases
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1111', '0000'))  # Output: '1111'
print(string_xor('1010', '1010'))  # Output: '0000'
```