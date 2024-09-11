```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings a and b.
    
    Args:
    a (str): First binary string consisting of 1s and 0s.
    b (str): Second binary string consisting of 1s and 0s.
    
    Returns:
    str: Binary XOR result of a and b.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the input strings
    for i, j in zip(a, b):
        # Perform XOR operation on corresponding bits
        # 1 XOR 1 = 0
        # 1 XOR 0 = 1
        # 0 XOR 1 = 1
        # 0 XOR 0 = 0
        result += str((int(i) ^ int(j)))
    
    # If the input strings are of different lengths
    # Pad the shorter string with zeros
    result += ''.join('0' for _ in range(abs(len(a) - len(b))))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: 100
```

In this script, the function `string_xor` takes two binary strings `a` and `b` as input and returns their binary XOR result. The XOR operation is performed by iterating over the input strings, performing the XOR operation on corresponding bits, and storing the result in a new string. If the input strings are of different lengths, the shorter string is padded with zeros to match the length of the longer string.