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
        str: The result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings")

    # Use map to apply XOR operation on the input strings
    # The XOR operation is performed by adding two strings and taking the modulus by 2
    # If the result is 2, it is converted back to 0
    return ''.join(map(lambda x, y: str((int(x) + int(y)) % 2), a, b))


# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
print(string_xor('111', '000'))  # Outputs: '111'
print(string_xor('101', '101'))  # Outputs: '000'
```