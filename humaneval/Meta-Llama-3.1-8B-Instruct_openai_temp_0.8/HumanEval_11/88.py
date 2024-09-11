```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of binary XOR operation as a string.
    """
    
    # Check if both inputs are valid binary strings
    if set(a).issubset({ '0', '1' }) and set(b).issubset({ '0', '1' }):
        # Initialize an empty result string
        result = ''
        
        # Iterate over the characters in the input strings
        for x, y in zip(a, b):
            # Perform XOR operation and append the result to the string
            result += str(int(x) ^ int(y))
        
        # If one string is longer than the other, append the remaining characters
        while len(a) > len(b):
            result += a[-1]
            a = a[:-1]
        while len(b) > len(a):
            result += b[-1]
            b = b[:-1]
        
        return result
    else:
        raise ValueError("Both inputs must be binary strings consisting of 1s and 0s")

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```