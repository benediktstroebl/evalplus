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
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Initialize an empty result string
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Check if characters are either '0' or '1'
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")
        
        # Perform XOR operation and append result to the result string
        result += str(int(char_a) ^ int(char_b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function `string_xor` that performs binary XOR on two input strings `a` and `b` consisting only of 1s and 0s. It first checks if both strings have the same length, then iterates over the characters in the input strings, checks if they are either '0' or '1', performs the XOR operation, and finally returns the result as a string.