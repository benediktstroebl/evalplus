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
    
    # Check if both inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Both input strings must be of equal length")
    
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both input strings must consist only of 1s and 0s")
    
    # Use zip to iterate over the characters of both strings in parallel
    # Use a list comprehension to perform the XOR operation and convert the result to a string
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input and returns the result of the binary XOR operation as a string. It checks for errors in the input and uses a list comprehension to perform the XOR operation on the characters of the input strings. The example usage at the end demonstrates how to use the function.