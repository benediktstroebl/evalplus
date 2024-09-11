```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First input string consisting only of 1s and 0s.
        b (str): Second input string consisting only of 1s and 0s.

    Returns:
        str: Result of binary XOR operation on inputs a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Ensure a and b are of equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Perform XOR operation on corresponding bits
    for bit_a, bit_b in zip(a, b):
        # XOR of 0 and 0 is 0, XOR of 1 and 1 is 0, XOR of 0 and 1 (or 1 and 0) is 1
        result += '1' if bit_a!= bit_b else '0'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. The XOR operation is performed by iterating over corresponding bits in `a` and `b`.