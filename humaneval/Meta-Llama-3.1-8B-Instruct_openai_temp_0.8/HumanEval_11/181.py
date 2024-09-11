```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.
    
    Returns:
        str: Result of binary XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Use the bitwise XOR operator (^) to perform XOR on corresponding bits
    # The result is then converted to a string
    return ''.join('1' if (int(a[i]) + int(b[i])) % 2 == 1 else '0' for i in range(len(a)))

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '110'))  # Expected output: '011'
```

This Python script defines a function `string_xor` that performs binary XOR operation on two input strings `a` and `b`. The function checks if both inputs consist only of 1s and 0s, and if not, it raises a `ValueError`. The XOR operation is performed using the bitwise XOR operator (`^`). The result is then converted to a string and returned.