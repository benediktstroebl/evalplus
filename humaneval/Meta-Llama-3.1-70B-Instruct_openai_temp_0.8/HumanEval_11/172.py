```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if inputs are valid (consist only of 1s and 0s)
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")
    
    # Initialize result string
    result = ''
    
    # Perform XOR operation for each character in the input strings
    for i in range(max(len(a), len(b))):
        # Handle different lengths by using '0' as a default value
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'
        
        # XOR operation: '1' if bits are different, '0' if bits are the same
        result += '1' if (bit_a!= bit_b) else '0'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```