### Binary String XOR
#### Problem Description

Perform binary XOR operation on two given binary strings.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two given binary strings.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current bits
        # 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0
        result += str(int(char_a) ^ int(char_b))
    
    # If one string is shorter than the other, append the remaining bits
    result += a[len(b):] if len(a) > len(b) else b[len(a):]
    
    return result
```