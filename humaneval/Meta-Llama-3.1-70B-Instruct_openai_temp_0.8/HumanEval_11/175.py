```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of binary XOR operation as a string.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s.")
    
    # Use zip to iterate over both strings in parallel
    # Use a generator expression to perform XOR on each pair of bits
    # Convert the result to a string using join
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input and returns the result of binary XOR operation as a string. The function first checks if both strings have the same length and consist only of 1s and 0s. Then it uses the `zip` function to iterate over both strings in parallel and performs XOR on each pair of bits using a generator expression. Finally, it converts the result to a string using `join`. The script also includes an example usage of the function.