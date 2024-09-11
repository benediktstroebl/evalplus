```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary string result of XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of equal length")

    # Use zip to iterate over two strings simultaneously
    # and use a list comprehension to perform XOR operation
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '010'))  # Expected output: '111'
```