```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Use the XOR operator on each pair of corresponding bits
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '110'))  # Expected output: '011'
```

This script defines the `string_xor` function, which takes two binary strings as input and returns their XOR result as a string. It includes a check to ensure the input strings have the same length, and it uses a generator expression to perform the XOR operation on each pair of corresponding bits. The script also includes example usage and test cases to demonstrate the function's behavior.