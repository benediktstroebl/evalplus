```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings")
    
    # Use the zip function to pair corresponding bits from both strings
    # and the join function to convert the result back to a string
    return ''.join('1' if a_bit!= b_bit else '0' for a_bit, b_bit in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR result. It also includes a test section to verify the correctness of the function.