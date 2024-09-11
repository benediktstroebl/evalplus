```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")

    # Use list comprehension to perform XOR operation on corresponding bits
    result = ['1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0' 
              for bit_a, bit_b in zip(a, b)]

    # Join the list into a string
    return ''.join(result)

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their result as a string. The function uses list comprehension to iterate over corresponding bits of the input strings, performs the XOR operation on each pair of bits, and joins the result into a string. The script also includes example usage and a test case.