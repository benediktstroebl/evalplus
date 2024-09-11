```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): First binary string
    b (str): Second binary string

    Returns:
    str: Binary XOR result of a and b as a string
    """
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Check if inputs contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip to iterate over characters of both strings in parallel
    # Use XOR operator (^) to calculate the XOR of each pair of characters
    # Convert the result back to a string using join
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test cases
print(string_xor('010', '110'))  # '100'
print(string_xor('111', '111'))  # '000'
print(string_xor('101', '010'))  # '111'
```