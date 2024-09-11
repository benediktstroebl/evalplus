```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both inputs are strings consisting only of 1s and 0s
    if not (set(a) <= {'0', '1'} and set(b) <= {'0', '1'}):
        raise ValueError("Both inputs must consist only of 1s and 0s.")
    
    # Check if both inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must have the same length.")
    
    # Use the zip function to iterate over both strings simultaneously
    # Use a generator expression to perform the XOR operation on each pair of bits
    # Convert the result to a string using the join method
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Example usage with error handling
try:
    print(string_xor('101', '111'))
except ValueError as e:
    print(e)
```