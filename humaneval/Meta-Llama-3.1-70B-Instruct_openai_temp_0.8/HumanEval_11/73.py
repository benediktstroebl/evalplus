```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    Both strings should only consist of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings should have the same length")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR operation on the current bits and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Example usage
print(string_xor('010', '110'))  # Outputs: 100

# Test cases
print(string_xor('0', '0'))  # Outputs: 0
print(string_xor('1', '1'))  # Outputs: 0
print(string_xor('1', '0'))  # Outputs: 1
print(string_xor('101', '110'))  # Outputs: 011
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. It also includes example usage and test cases to demonstrate the function's behavior.