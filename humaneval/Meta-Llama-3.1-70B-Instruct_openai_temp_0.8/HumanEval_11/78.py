```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): A string of 1s and 0s.
        b (str): A string of 1s and 0s.

    Returns:
        str: The result of binary XOR on inputs a and b.

    Raises:
        ValueError: If the lengths of input strings a and b are not equal.
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```