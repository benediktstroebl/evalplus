```python
from typing import List

def int_to_binary_list(n: int) -> List[int]:
    """Convert an integer to a binary list representation"""
    return [int(i) for i in bin(n)[2:]]

def binary_list_to_int(binary_list: List[int]) -> int:
    """Convert a binary list to an integer"""
    return int(''.join(map(str, binary_list)), 2)

def string_xor(a: str, b: str) -> str:
    """Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform XOR operation
    xor_result = int_a ^ int_b
    
    # Convert result back to a binary string
    binary_result = bin(xor_result)[2:]
    
    # Pad the result with leading zeros to match the length of the longest input
    max_length = max(len(a), len(b))
    padded_result = binary_result.zfill(max_length)
    
    return padded_result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```