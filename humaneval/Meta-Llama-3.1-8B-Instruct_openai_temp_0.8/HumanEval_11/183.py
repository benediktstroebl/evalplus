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
    str: The result of binary XOR operation on a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use list comprehension with XOR operation to generate result
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))
```

You can test the function using:
```python
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('111', '000'))  # Expected output: '111'
print(string_xor('101', '101'))  # Expected output: '000'
```