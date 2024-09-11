### Binary String XOR
#### Problem Description
Perform binary XOR operation on two binary strings.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a binary string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize result string
    result = ''
    
    # Perform XOR operation on each pair of corresponding bits
    for bit_a, bit_b in zip(a, b):
        # If bits are different, append '1' to the result
        if bit_a!= bit_b:
            result += '1'
        # If bits are the same, append '0' to the result
        else:
            result += '0'
    
    return result
```

#### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('111', '000'))  # Output: '111'
```