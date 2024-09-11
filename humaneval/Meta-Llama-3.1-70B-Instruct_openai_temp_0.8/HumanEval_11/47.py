```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    Both strings should consist only of 1s and 0s.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings should have the same length")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings should consist only of 1s and 0s")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Should print '100'
```