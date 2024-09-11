### Binary String XOR
#### Python Script

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of XOR operation as a binary string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Use list comprehension to apply XOR operation
    result = [str(int(x) ^ int(y)) for x, y in zip(a, b)]
    
    # Remove any leading zeros
    result = ''.join(result).lstrip('0') or '0'
    
    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('1010', '1100'))  # Output: '0110'
```