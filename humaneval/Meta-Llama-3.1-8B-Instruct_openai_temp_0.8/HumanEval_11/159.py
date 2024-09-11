```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A binary string consisting of 1s and 0s.
    b (str): A binary string consisting of 1s and 0s.

    Returns:
    str: The binary XOR of a and b as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Convert input strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform binary XOR
    xor_result = int_a ^ int_b
    
    # Convert result back to binary string
    bin_result = bin(xor_result)[2:]
    
    # Pad result with leading zeros to match input lengths
    max_len = max(len(a), len(b))
    bin_result = bin_result.zfill(max_len)
    
    return bin_result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a binary string. It includes docstrings for documentation and example use cases. The script also includes test cases at the end to demonstrate the function's behavior.